import csv
import logging
import json
from pathlib import Path
from pydantic import ValidationError
from logging.handlers import RotatingFileHandler
from validator.model import PurchaseOrderModel

def process_purchase_orders():
    valid_records = []
    passed = 0
    failed = 0
    
    # Paths
    INPUT_CSV = Path("Day_03/data/input/purchase_orders_raw.csv")
    OUTPUT_JSON = Path("Day_03/data/output/valid_orders.json")
    ERRORS_LOG = Path("Day_03/data/output/errors_log.log")
    
    # Setup Logger
    logger = logging.getLogger("ErrorLogger")
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    # Attach Stream Handler (Console output)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    # Attach Rotating File Handler (File output)
    log_file_handler = RotatingFileHandler(
        ERRORS_LOG, maxBytes=50000, backupCount=2, encoding="utf-8"
    )
    log_file_handler.setLevel(logging.DEBUG)
    log_file_handler.setFormatter(formatter)
    logger.addHandler(log_file_handler)
    
    # Open purchase_orders_raw CSV file
    with INPUT_CSV.open(mode="r") as file:
        # Initialize the DictReader object
        csv_reader = csv.DictReader(file)
        
        # Loop through rows of file
        for row_number, row in enumerate(csv_reader, start=1):
            try:
                record = PurchaseOrderModel(**row)
                json_output = record.model_dump(mode="json")
                valid_records.append(json_output)
                
                 # Track counts for final pass/fail ratio
                passed+=1
                
            except ValidationError as exc:
                # Track counts for final pass/fail ratio
                failed+=1
               
                # On failure record the row number and show error
                logger.error(f"Row {row_number} REJECTED: {exc.errors()}")
                
        pass
    
    # On success add rows to json file 
    with OUTPUT_JSON.open("w") as f:
        json.dump(valid_records, f, indent=2)
                
        pass
    
    return valid_records, passed, failed

def create_summary(passed, failed):
    total_records = passed + failed
    print("\n\n==========[ S U M M A R Y ]==========\n\n")
    print(f"{passed}/{total_records} PASSED\n")
    print(f"{failed}/{total_records} FAILED\n")
    