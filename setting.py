from pathlib import Path

ROOT_DIR = Path(__file__).parent

LOG_FILENAME = ROOT_DIR / "logs" / "app.log"
if not LOG_FILENAME.parent.exists():
    LOG_FILENAME.parent.mkdir(parents=True, exist_ok=True)
    LOG_FILENAME.touch()
DB_PATH = ROOT_DIR / "db" / "database.db"
DEBUG = True
