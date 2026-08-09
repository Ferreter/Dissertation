# Legacy Gamma Page Capture

**Executable:** `scripts/legacy/disc-gamma.py`  
**Status:** Legacy exploratory work retained for provenance.

## Purpose

I used this script to test whether a full public gamma-exposure page could be captured and delivered to Discord.

## Workflow

```mermaid
flowchart LR
    A["Legacy browser page"] --> B["Experimental full-page capture and message flow"]
    B --> C["Local image or message"]
    C --> D["Provenance only"]
```

## Inputs

- The public NVDA gamma-exposure webpage.
- `DISCORD_WEBHOOK_URL` loaded locally from `main.env`.
- A Playwright Chromium installation.

## Processing and rationale

- Open a visible Chromium session and wait for the page to load.
- Accept the cookie prompt when it appears.
- Save a full-page screenshot, then upload the saved file through the configured webhook.

## Outputs

- A local, untracked full-page capture when the experiment is run.
- An optional Discord message containing the image; neither item is maintained dissertation evidence.

## Representative outputs

No maintained artifact is expected. The experimental implementation remains in the [legacy script](../../../scripts/legacy/disc-gamma.py) as provenance only.

## Findings and decisions

- The approach was useful as a browser-automation experiment but was not adopted as a dissertation data source.
- I moved the webhook out of the code so no credential is stored in the repository.

## Limitations

- The page layout, cookie selector and anti-automation behaviour can change.
- A screenshot is not a structured, reproducible historical dataset.

## Next steps

- Keep this script separate from the main pipeline and prefer licensed API data for research evidence.
