from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT / "data"
INPUT_DIR = DATA_DIR / "input"
OUTPUT_DIR = DATA_DIR / "output"

INPUT_CSV = INPUT_DIR / "purchase_orders_raw.csv"
OUTPUT_JSON = OUTPUT_DIR / "valid_orders.json"
ERROR_LOG = OUTPUT_DIR / "errors_log.log"