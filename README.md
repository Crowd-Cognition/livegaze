# Live Gaze

Live Gaze is a system to analyze eye gaze of multiple people on surfaces in real-time.

## Local setup (Docker)

```bash
cd livegaze
cp .env.example .env   # create and fill in secrets if .env does not exist yet
mkdir -p data/artworks
docker compose up --build
```

Open the web UI at **http://127.0.0.1:5100**

## Live Gaze Companion — connection

### Local server

1. Start Docker (`docker compose up`).
2. Find your computer's local network IP (not `127.0.0.1` if the Companion runs on a phone):
   - macOS: **System Settings → Network → Wi‑Fi → Details**, or `ipconfig getifaddr en0`
3. In **Live Gaze Companion**, enter: `<your-ip>:5100`  
   Example: `192.168.1.42:5100`
4. Phone and computer must be on the **same Wi‑Fi**.

### Production (livegaze.co)

- Web UI: **https://livegaze.co**
- Companion: connect to **`livegaze.co`** (HTTPS, no port suffix)

## Viewing gaze on a board

Gaze dots appear on the full-screen board view, not on the main dashboard.

Open a board via **Edit** or go to `/boards/simple_js/<board_id>`.

## Deploying to livegaze.co

SSH into the server:

```bash
chmod 400 /path/to/LiveGazePair.pem
ssh -i /path/to/LiveGazePair.pem ubuntu@89.47.190.100
```

On the server:

```bash
cd ~/livegaze
git pull origin main
sudo docker compose build
sudo docker compose up -d
sudo docker compose ps
```

## Services

| Service  | Port (local)        |
|----------|---------------------|
| Flask    | 127.0.0.1:5100      |
| Postgres | 127.0.0.1:5433      |
| Redis    | 127.0.0.1:6379      |
