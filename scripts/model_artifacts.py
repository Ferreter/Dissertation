"""Save and verify dissertation model artifacts with reproducible metadata.

The modelling notebooks use these helpers after their development-only refit.
Model files are written atomically so an interrupted rerun does not replace a
valid artifact with a partial file.
"""

from __future__ import annotations

import hashlib
import json
import os
import tempfile
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Mapping, Sequence

import joblib


def sha256_file(path: Path | str) -> str:
    """Return the SHA-256 digest for a saved artifact."""
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _json_safe(value: Any) -> Any:
    """Convert numpy-like scalars and nested values into JSON-safe objects."""
    if isinstance(value, Mapping):
        return {str(key): _json_safe(item) for key, item in value.items()}
    if isinstance(value, (list, tuple, set)):
        return [_json_safe(item) for item in value]
    if isinstance(value, Path):
        return value.as_posix()
    if hasattr(value, "item"):
        try:
            return value.item()
        except (TypeError, ValueError):
            pass
    if isinstance(value, (str, int, float, bool)) or value is None:
        return value
    return str(value)


def _atomic_joblib_dump(value: Any, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    handle = tempfile.NamedTemporaryFile(
        prefix=f".{destination.stem}-",
        suffix=destination.suffix,
        dir=destination.parent,
        delete=False,
    )
    temporary = Path(handle.name)
    handle.close()
    try:
        joblib.dump(value, temporary)
        os.replace(temporary, destination)
    finally:
        temporary.unlink(missing_ok=True)


def save_sklearn_artifact(
    estimator: Any,
    destination: Path | str,
    metadata: Mapping[str, Any],
    *,
    relative_to: Path | str | None = None,
    verification_input: Any | None = None,
) -> dict[str, Any]:
    """Save a fitted scikit-learn estimator and verify that it reloads."""
    destination = Path(destination)
    _atomic_joblib_dump(estimator, destination)
    reloaded = joblib.load(destination)
    if not hasattr(reloaded, "predict"):
        raise TypeError(f"Reloaded artifact has no predict method: {destination}")
    verified_prediction = False
    if verification_input is not None:
        reloaded.predict(verification_input)
        verified_prediction = True
    recorded_path = (
        destination.relative_to(Path(relative_to)).as_posix()
        if relative_to is not None
        else destination.as_posix()
    )
    return {
        **_json_safe(metadata),
        "artifact_format": "joblib",
        "artifact_path": recorded_path,
        "artifact_sha256": sha256_file(destination),
        "verified_reload": True,
        "verified_prediction": verified_prediction,
    }


def save_keras_artifact(
    model: Any,
    model_destination: Path | str,
    scaler: Any,
    scaler_destination: Path | str,
    metadata: Mapping[str, Any],
    keras_loader: Callable[[str], Any],
    *,
    relative_to: Path | str | None = None,
    verification_input: Any | None = None,
) -> dict[str, Any]:
    """Save a Keras model and fitted scaler, then verify both reload."""
    model_destination = Path(model_destination)
    scaler_destination = Path(scaler_destination)
    model_destination.parent.mkdir(parents=True, exist_ok=True)
    scaler_destination.parent.mkdir(parents=True, exist_ok=True)

    temporary_model = model_destination.with_name(
        f".{model_destination.stem}-{uuid.uuid4().hex}.keras"
    )
    try:
        model.save(temporary_model)
        os.replace(temporary_model, model_destination)
    finally:
        temporary_model.unlink(missing_ok=True)

    _atomic_joblib_dump(scaler, scaler_destination)
    reloaded_model = keras_loader(str(model_destination))
    reloaded_scaler = joblib.load(scaler_destination)
    if not hasattr(reloaded_model, "predict"):
        raise TypeError(f"Reloaded Keras model has no predict method: {model_destination}")
    if not hasattr(reloaded_scaler, "transform"):
        raise TypeError(f"Reloaded scaler has no transform method: {scaler_destination}")
    verified_prediction = False
    if verification_input is not None:
        reloaded_model.predict(verification_input, verbose=0)
        verified_prediction = True

    recorded_model_path = (
        model_destination.relative_to(Path(relative_to)).as_posix()
        if relative_to is not None
        else model_destination.as_posix()
    )
    recorded_scaler_path = (
        scaler_destination.relative_to(Path(relative_to)).as_posix()
        if relative_to is not None
        else scaler_destination.as_posix()
    )
    return {
        **_json_safe(metadata),
        "artifact_format": "keras",
        "artifact_path": recorded_model_path,
        "artifact_sha256": sha256_file(model_destination),
        "scaler_path": recorded_scaler_path,
        "scaler_sha256": sha256_file(scaler_destination),
        "verified_reload": True,
        "verified_prediction": verified_prediction,
    }


def write_model_manifest(
    destination: Path | str,
    artifacts: Sequence[Mapping[str, Any]],
    metadata: Mapping[str, Any] | None = None,
) -> Path:
    """Write the shared model manifest atomically."""
    destination = Path(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "schema_version": 1,
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        **_json_safe(metadata or {}),
        "artifacts": _json_safe(list(artifacts)),
    }
    handle = tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        prefix=f".{destination.stem}-",
        suffix=".json",
        dir=destination.parent,
        delete=False,
    )
    temporary = Path(handle.name)
    try:
        json.dump(payload, handle, indent=2)
        handle.write("\n")
        handle.close()
        os.replace(temporary, destination)
    finally:
        if not handle.closed:
            handle.close()
        temporary.unlink(missing_ok=True)
    return destination
