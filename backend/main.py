from datetime import datetime, timezone
from uuid import uuid4

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Recon Platform API", version="0.1.0")


class ScanRequest(BaseModel):
    asset: str = Field(..., description="Hostname, IP, or application identifier")
    scan_type: str = Field(default="baseline", description="Requested scan profile")


class ScanTask(BaseModel):
    scan_id: str
    status: str
    message: str
    created_at: datetime


scan_results_store: dict[str, dict[str, str | dict[str, str]]] = {}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/scans/start", response_model=ScanTask)
def start_scan(payload: ScanRequest) -> ScanTask:
    scan_id = str(uuid4())
    created_at = datetime.now(timezone.utc)

    scan_results_store[scan_id] = {
        "asset": payload.asset,
        "scan_type": payload.scan_type,
        "status": "queued",
        "summary": "Placeholder result. Integrate worker pipeline to populate findings.",
    }

    return ScanTask(
        scan_id=scan_id,
        status="queued",
        message="Scan task created. Replace placeholder with async task queue integration.",
        created_at=created_at,
    )


@app.get("/scans/{scan_id}/results")
def fetch_scan_results(scan_id: str) -> dict[str, str | dict[str, str]]:
    result = scan_results_store.get(scan_id)
    if not result:
        return {
            "scan_id": scan_id,
            "status": "not_found",
            "summary": "No scan result found. Replace placeholder with persistent storage lookup.",
        }

    return {"scan_id": scan_id, "result": result}
