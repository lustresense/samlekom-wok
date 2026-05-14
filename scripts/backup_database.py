import os
import sqlite3
import sys
from datetime import datetime
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]
DEFAULT_DB_PATH = ROOT_DIR / "database" / "runtime" / "database.db"
DEFAULT_BACKUP_DIR = ROOT_DIR / "database" / "backups"


def resolve_path(raw_value, default_path):
  if not raw_value:
    return default_path
  path = Path(raw_value)
  if not path.is_absolute():
    path = ROOT_DIR / path
  return path.resolve()


def main():
  check_only = "--check" in sys.argv[1:]
  db_path = resolve_path(os.environ.get("SIMRP_DB_PATH"), DEFAULT_DB_PATH)
  backup_dir = resolve_path(os.environ.get("SIMRP_BACKUP_DIR"), DEFAULT_BACKUP_DIR)

  if check_only:
    print(f"DB: {db_path}")
    print(f"Backup dir: {backup_dir}")
    if not db_path.exists():
      print("WARN: database file does not exist yet")
    return 0

  if not db_path.exists():
    print(f"ERROR: database file not found: {db_path}", file=sys.stderr)
    return 1

  backup_dir.mkdir(parents=True, exist_ok=True)
  timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
  backup_path = backup_dir / f"simrp_backup_{timestamp}.db"

  source = sqlite3.connect(str(db_path))
  try:
    target = sqlite3.connect(str(backup_path))
    try:
      source.backup(target)
    finally:
      target.close()
  finally:
    source.close()

  print(f"SUCCESS: Backup completed: {backup_path}")
  return 0


if __name__ == "__main__":
  raise SystemExit(main())
