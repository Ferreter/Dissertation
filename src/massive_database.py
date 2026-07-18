
from __future__ import annotations

import random
import time
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable, Iterator, Optional
from urllib.parse import quote

import duckdb
import pandas as pd
import requests


BASE_URL = "https://api.massive.com"


class MassiveAPIError(RuntimeError):
    pass


@dataclass(frozen=True)
class DownloadResult:
    dataset: str
    ticker: str
    session_date: str
    rows: int
    file_path: Optional[str]
    status: str
    message: str = ""


class MassiveREST:
    """REST wrapper with retries, rate-limit handling and pagination."""

    def __init__(
        self,
        api_key: str,
        base_url: str = BASE_URL,
        timeout_seconds: int = 60,
        max_retries: int = 6,
    ) -> None:
        if not api_key:
            raise ValueError("A Massive API key is required.")
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.timeout_seconds = timeout_seconds
        self.max_retries = max_retries
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Accept": "application/json",
                "User-Agent": "dissertation-massive-database/1.0",
            }
        )

    def _request(self, path_or_url: str, params: Optional[dict[str, Any]] = None):
        url = path_or_url if path_or_url.startswith("http") else f"{self.base_url}/{path_or_url.lstrip('/')}"
        query = dict(params or {})
        query.setdefault("apiKey", self.api_key)
        last_error = None

        for attempt in range(self.max_retries + 1):
            try:
                response = self.session.get(url, params=query, timeout=self.timeout_seconds)
                if response.status_code == 429:
                    retry_after = response.headers.get("Retry-After")
                    wait = float(retry_after) if retry_after else min(60.0, 2**attempt + random.random())
                    time.sleep(wait)
                    continue
                if 500 <= response.status_code < 600:
                    time.sleep(min(60.0, 2**attempt + random.random()))
                    continue
                return response
            except requests.RequestException as exc:
                last_error = exc
                if attempt >= self.max_retries:
                    break
                time.sleep(min(60.0, 2**attempt + random.random()))

        raise MassiveAPIError(f"Request failed after retries: {url}. Last error: {last_error}")

    @staticmethod
    def _message(response) -> str:
        try:
            payload = response.json()
            return str(payload.get("error") or payload.get("message") or payload)
        except Exception:
            return response.text[:500]

    def get_json(self, path_or_url: str, params: Optional[dict[str, Any]] = None) -> dict[str, Any]:
        response = self._request(path_or_url, params)
        if not response.ok:
            raise MassiveAPIError(
                f"Massive API returned HTTP {response.status_code}: {self._message(response)}"
            )
        return response.json()

    def probe(self, path: str, params: Optional[dict[str, Any]] = None) -> dict[str, Any]:
        response = self._request(path, params)
        try:
            payload = response.json()
        except Exception:
            payload = response.text[:500]
        return {
            "path": path,
            "http_status": response.status_code,
            "ok": response.ok,
            "payload": payload,
        }

    def paginate(
        self,
        path: str,
        params: Optional[dict[str, Any]] = None,
        max_pages: Optional[int] = None,
    ) -> Iterator[dict[str, Any]]:
        next_url = path
        next_params = dict(params or {})
        page = 0

        while next_url:
            payload = self.get_json(next_url, next_params)
            page += 1
            yield from (payload.get("results") or [])
            if max_pages is not None and page >= max_pages:
                break
            next_url = payload.get("next_url")
            next_params = {}

    def aggregates(
        self,
        ticker: str,
        from_date: str,
        to_date: str,
        multiplier: int = 1,
        timespan: str = "minute",
        adjusted: bool = True,
        limit: int = 50_000,
    ) -> list[dict[str, Any]]:
        path = (
            f"/v2/aggs/ticker/{quote(ticker, safe=':')}/range/"
            f"{multiplier}/{timespan}/{from_date}/{to_date}"
        )
        payload = self.get_json(
            path,
            {
                "adjusted": str(adjusted).lower(),
                "sort": "asc",
                "limit": limit,
            },
        )
        return payload.get("results") or []

    def option_contracts(
        self,
        underlying_ticker: str,
        as_of: Optional[str] = None,
        expiration_date_gte: Optional[str] = None,
        expiration_date_lte: Optional[str] = None,
        strike_price_gte: Optional[float] = None,
        strike_price_lte: Optional[float] = None,
        contract_type: Optional[str] = None,
        expired: Optional[bool] = None,
        limit: int = 1_000,
        max_pages: Optional[int] = None,
    ) -> list[dict[str, Any]]:
        params: dict[str, Any] = {
            "underlying_ticker": underlying_ticker,
            "limit": limit,
            "sort": "ticker",
            "order": "asc",
        }
        optional = {
            "as_of": as_of,
            "expiration_date.gte": expiration_date_gte,
            "expiration_date.lte": expiration_date_lte,
            "strike_price.gte": strike_price_gte,
            "strike_price.lte": strike_price_lte,
            "contract_type": contract_type,
            "expired": str(expired).lower() if expired is not None else None,
        }
        params.update({k: v for k, v in optional.items() if v is not None})
        return list(self.paginate("/v3/reference/options/contracts", params, max_pages))

    def option_chain_snapshot(
        self,
        underlying_asset: str,
        expiration_date_gte: Optional[str] = None,
        expiration_date_lte: Optional[str] = None,
        strike_price_gte: Optional[float] = None,
        strike_price_lte: Optional[float] = None,
        contract_type: Optional[str] = None,
        limit: int = 250,
        max_pages: Optional[int] = None,
    ) -> list[dict[str, Any]]:
        params: dict[str, Any] = {"limit": limit}
        optional = {
            "expiration_date.gte": expiration_date_gte,
            "expiration_date.lte": expiration_date_lte,
            "strike_price.gte": strike_price_gte,
            "strike_price.lte": strike_price_lte,
            "contract_type": contract_type,
        }
        params.update({k: v for k, v in optional.items() if v is not None})
        path = f"/v3/snapshot/options/{quote(underlying_asset, safe=':')}"
        return list(self.paginate(path, params, max_pages))


def iter_business_days(start_date: str, end_date: str) -> list[str]:
    return [d.strftime("%Y-%m-%d") for d in pd.bdate_range(start_date, end_date)]


def normalize_aggregates(
    records: list[dict[str, Any]],
    ticker: str,
    asset_class: str,
) -> pd.DataFrame:
    columns = [
        "ticker",
        "asset_class",
        "timestamp_ms",
        "timestamp_utc",
        "timestamp_et",
        "session_date",
        "open",
        "high",
        "low",
        "close",
        "volume",
        "vwap",
        "transactions",
        "otc",
    ]
    if not records:
        return pd.DataFrame(columns=columns)

    frame = pd.DataFrame(records).rename(
        columns={
            "t": "timestamp_ms",
            "o": "open",
            "h": "high",
            "l": "low",
            "c": "close",
            "v": "volume",
            "vw": "vwap",
            "n": "transactions",
        }
    )
    frame["ticker"] = ticker
    frame["asset_class"] = asset_class
    frame["timestamp_utc"] = pd.to_datetime(frame["timestamp_ms"], unit="ms", utc=True)
    local_et = frame["timestamp_utc"].dt.tz_convert("America/New_York")
    frame["session_date"] = local_et.dt.strftime("%Y-%m-%d")
    # Store New York wall-clock time without timezone metadata for reliable
    # DuckDB TIME filtering; timestamp_utc remains the canonical instant.
    frame["timestamp_et"] = local_et.dt.tz_localize(None)

    for name in columns:
        if name not in frame:
            frame[name] = pd.NA

    return (
        frame[columns]
        .sort_values("timestamp_utc")
        .drop_duplicates(["ticker", "timestamp_ms"], keep="last")
        .reset_index(drop=True)
    )


def normalize_option_contracts(records: list[dict[str, Any]], as_of: str) -> pd.DataFrame:
    if not records:
        return pd.DataFrame()
    frame = pd.json_normalize(records, sep="_")
    frame["as_of"] = as_of
    preferred = [
        "ticker",
        "underlying_ticker",
        "contract_type",
        "exercise_style",
        "expiration_date",
        "strike_price",
        "shares_per_contract",
        "primary_exchange",
        "cfi",
        "as_of",
    ]
    first = [c for c in preferred if c in frame.columns]
    return frame[first + [c for c in frame.columns if c not in first]]


def normalize_option_chain(
    records: list[dict[str, Any]],
    collected_at: Optional[datetime] = None,
) -> pd.DataFrame:
    if not records:
        return pd.DataFrame()
    frame = pd.json_normalize(records, sep="_")
    stamp = pd.Timestamp(collected_at or datetime.utcnow(), tz="UTC")
    frame["collected_at_utc"] = stamp
    frame["snapshot_date"] = stamp.strftime("%Y-%m-%d")
    return frame


def safe_ticker_name(ticker: str) -> str:
    return ticker.replace(":", "_").replace("/", "_")


def write_daily_parquet(
    frame: pd.DataFrame,
    root: Path | str,
    dataset: str,
    ticker: str,
    session_date: str,
) -> Path:
    if frame.empty:
        raise ValueError("Cannot write an empty DataFrame.")
    directory = (
        Path(root)
        / "raw"
        / dataset
        / f"ticker={safe_ticker_name(ticker)}"
        / f"date={session_date}"
    )
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / "data.parquet"
    frame.to_parquet(path, index=False)
    return path


def write_snapshot_parquet(
    frame: pd.DataFrame,
    root: Path | str,
    dataset: str,
    snapshot_date: str,
    filename: str,
) -> Path:
    if frame.empty:
        raise ValueError("Cannot write an empty DataFrame.")
    directory = Path(root) / "raw" / dataset / f"snapshot_date={snapshot_date}"
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / filename
    frame.to_parquet(path, index=False)
    return path


def initialize_duckdb(db_path: Path | str):
    db_path = Path(db_path)
    db_path.parent.mkdir(parents=True, exist_ok=True)
    con = duckdb.connect(str(db_path))
    con.execute(
        """
        CREATE TABLE IF NOT EXISTS ingestion_log (
            dataset VARCHAR,
            ticker VARCHAR,
            session_date DATE,
            rows BIGINT,
            file_path VARCHAR,
            status VARCHAR,
            message VARCHAR,
            ingested_at_utc TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (dataset, ticker, session_date)
        )
        """
    )
    return con


def log_download(con, result: DownloadResult) -> None:
    con.execute(
        """
        INSERT OR REPLACE INTO ingestion_log
        (dataset, ticker, session_date, rows, file_path, status, message, ingested_at_utc)
        VALUES (?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
        """,
        [
            result.dataset,
            result.ticker,
            result.session_date,
            result.rows,
            result.file_path,
            result.status,
            result.message,
        ],
    )


def download_aggregate_history(
    client: MassiveREST,
    con,
    data_root: Path | str,
    ticker: str,
    asset_class: str,
    start_date: str,
    end_date: str,
    multiplier: int = 1,
    timespan: str = "minute",
    overwrite: bool = False,
) -> list[DownloadResult]:
    dataset = f"{asset_class}_{timespan}_{multiplier}"
    output: list[DownloadResult] = []

    for session_date in iter_business_days(start_date, end_date):
        previous = con.execute(
            """
            SELECT status FROM ingestion_log
            WHERE dataset = ? AND ticker = ? AND session_date = ?
            """,
            [dataset, ticker, session_date],
        ).fetchone()

        if previous and previous[0] == "ok" and not overwrite:
            output.append(
                DownloadResult(dataset, ticker, session_date, 0, None, "skipped", "Already downloaded")
            )
            continue

        try:
            raw = client.aggregates(
                ticker,
                session_date,
                session_date,
                multiplier=multiplier,
                timespan=timespan,
            )
            frame = normalize_aggregates(raw, ticker, asset_class)
            if frame.empty:
                result = DownloadResult(dataset, ticker, session_date, 0, None, "empty", "No qualifying bars")
            else:
                path = write_daily_parquet(frame, data_root, dataset, ticker, session_date)
                result = DownloadResult(dataset, ticker, session_date, len(frame), str(path), "ok", "")
        except Exception as exc:
            result = DownloadResult(dataset, ticker, session_date, 0, None, "error", str(exc)[:1000])

        log_download(con, result)
        output.append(result)

    return output


def register_parquet_views(con, data_root: Path | str) -> list[str]:
    data_root = Path(data_root)
    created: list[str] = []

    datasets = [
        "stock_minute_1",
        "index_minute_1",
        "option_minute_1",
        "option_chain_snapshots",
        "option_contracts",
    ]

    for name in datasets:
        base = data_root / "raw" / name
        if base.exists() and any(base.rglob("*.parquet")):
            glob = str(base / "**" / "*.parquet").replace("\\", "/")
            con.execute(
                f"""
                CREATE OR REPLACE VIEW {name} AS
                SELECT *
                FROM read_parquet('{glob}', union_by_name=true, hive_partitioning=true)
                """
            )
            created.append(name)

    parts = [v for v in ["stock_minute_1", "index_minute_1"] if v in created]
    if parts:
        con.execute(
            "CREATE OR REPLACE VIEW underlying_minute_1 AS "
            + " UNION ALL ".join(f"SELECT * FROM {v}" for v in parts)
        )
        created.append("underlying_minute_1")

        con.execute(
            """
            CREATE OR REPLACE VIEW underlying_regular_session AS
            SELECT *
            FROM underlying_minute_1
            WHERE CAST(timestamp_et AS TIME) >= TIME '09:30:00'\n              AND CAST(timestamp_et AS TIME) < TIME '16:00:00'
            """
        )
        created.append("underlying_regular_session")

        con.execute(
            """
            CREATE OR REPLACE VIEW underlying_15min AS
            SELECT
                ticker,
                asset_class,
                time_bucket(INTERVAL '15 minutes', timestamp_utc) AS timestamp_utc,
                min(timestamp_et) AS timestamp_et,
                min(session_date) AS session_date,
                arg_min(open, timestamp_utc) AS open,
                max(high) AS high,
                min(low) AS low,
                arg_max(close, timestamp_utc) AS close,
                sum(volume) AS volume,
                CASE
                    WHEN sum(volume) > 0
                    THEN sum(coalesce(vwap, close) * volume) / sum(volume)
                    ELSE avg(coalesce(vwap, close))
                END AS vwap,
                sum(transactions) AS transactions
            FROM underlying_regular_session
            GROUP BY ticker, asset_class, time_bucket(INTERVAL '15 minutes', timestamp_utc)
            ORDER BY ticker, timestamp_utc
            """
        )
        created.append("underlying_15min")

    return created


def data_quality_report(frame: pd.DataFrame) -> dict[str, Any]:
    if frame.empty:
        return {"rows": 0, "duplicate_keys": 0, "missing_close": 0}
    return {
        "rows": int(len(frame)),
        "duplicate_keys": int(frame.duplicated(["ticker", "timestamp_ms"]).sum()),
        "missing_close": int(frame["close"].isna().sum()),
        "first_timestamp_utc": str(frame["timestamp_utc"].min()),
        "last_timestamp_utc": str(frame["timestamp_utc"].max()),
    }


def discover_option_underlying(
    client: MassiveREST,
    candidates: Iterable[str] = ("I:SPX", "SPX"),
    as_of: Optional[str] = None,
):
    checks = []
    for candidate in candidates:
        try:
            records = client.option_contracts(
                underlying_ticker=candidate,
                as_of=as_of,
                limit=10,
                max_pages=1,
            )
            checks.append(
                {"candidate": candidate, "contracts_returned": len(records), "status": "ok"}
            )
            if records:
                return candidate, pd.DataFrame(checks)
        except Exception as exc:
            checks.append(
                {"candidate": candidate, "contracts_returned": 0, "status": str(exc)}
            )
    return None, pd.DataFrame(checks)


def select_near_atm_contracts(
    contracts: pd.DataFrame,
    spot: float,
    max_contracts: int = 40,
    moneyness_pct: float = 0.05,
) -> pd.DataFrame:
    if contracts.empty:
        return contracts
    frame = contracts.copy()
    frame["strike_price"] = pd.to_numeric(frame["strike_price"], errors="coerce")
    frame = frame[
        frame["strike_price"].between(
            spot * (1 - moneyness_pct),
            spot * (1 + moneyness_pct),
        )
    ]
    frame["distance_to_spot"] = (frame["strike_price"] - spot).abs()
    cols = [c for c in ["expiration_date", "distance_to_spot", "contract_type"] if c in frame]
    return frame.sort_values(cols).head(max_contracts).reset_index(drop=True)


def latest_regular_session_price(
    con,
    ticker: str,
    session_date: str,
    at_or_before_et: str = "15:00:00",
) -> Optional[float]:
    row = con.execute(
        """
        SELECT close
        FROM underlying_regular_session
        WHERE ticker = ?
          AND session_date = ?
          AND CAST(timestamp_et AS TIME) <= CAST(? AS TIME)
        ORDER BY timestamp_utc DESC
        LIMIT 1
        """,
        [ticker, session_date, at_or_before_et],
    ).fetchone()
    return float(row[0]) if row else None


def download_selected_option_bars(
    client: MassiveREST,
    con,
    data_root: Path | str,
    contracts: pd.DataFrame,
    session_date: str,
    multiplier: int = 1,
    timespan: str = "minute",
    sleep_seconds: float = 0.0,
) -> pd.DataFrame:
    reports = []
    if contracts.empty:
        return pd.DataFrame()

    dataset = f"option_{timespan}_{multiplier}"
    for ticker in contracts["ticker"].dropna().astype(str):
        try:
            raw = client.aggregates(
                ticker,
                session_date,
                session_date,
                multiplier=multiplier,
                timespan=timespan,
            )
            frame = normalize_aggregates(raw, ticker, "option")
            if frame.empty:
                result = DownloadResult(dataset, ticker, session_date, 0, None, "empty", "No qualifying bars")
            else:
                path = write_daily_parquet(frame, data_root, dataset, ticker, session_date)
                result = DownloadResult(dataset, ticker, session_date, len(frame), str(path), "ok", "")
        except Exception as exc:
            result = DownloadResult(dataset, ticker, session_date, 0, None, "error", str(exc)[:500])

        log_download(con, result)
        reports.append(result.__dict__)
        if sleep_seconds:
            time.sleep(sleep_seconds)

    return pd.DataFrame(reports)
