# Recon

Project scaffold for a security vulnerability and asset management platform.

## Backend (FastAPI)

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Available placeholder endpoints:
- `POST /scans/start` - create a placeholder scan task
- `GET /scans/{scan_id}/results` - fetch placeholder scan results

## Frontend (Vue 3 + Vite)

```bash
cd frontend
npm install
npm run dev -- --host 0.0.0.0 --port 5173
```

The frontend includes a modern dashboard layout with a 2x2 grid of asset statistics cards.
