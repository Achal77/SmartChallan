from pathlib import Path

PROJECT_AUTHOR = "A Achal"
REGISTRATION_NO = "24BAI10839"
PROJECT_TITLE = "SmartChallan"

SNAPSHOTS_DIR = Path("snapshots")
CHALLANS_DIR = Path("challans")
LOGS_DIR = Path("logs")
LOG_FILE = LOGS_DIR / "detections.csv"
LOG_COLUMNS = ["timestamp", "violation", "plate", "confidence", "challan_id", "snapshot"]
DEMO_PLATE = REGISTRATION_NO


def ensure_runtime_directories() -> None:
    for directory in (SNAPSHOTS_DIR, CHALLANS_DIR, LOGS_DIR):
        directory.mkdir(parents=True, exist_ok=True)
