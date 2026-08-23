import csv
import json
import logging
from pydantic import ValidationError
from validator.model import PurchaseOrderModel

logger = logging.getLogger(__name__)

def process_purchase_orders(input_csv_path, output_json_path):
    valid_records = []
    passed = 0
    failed = 0
    
    # Open purchase_orders_raw CSV file
    with input_csv_path.open(mode="r", encoding="utf-8", newline="") as file:
        # Initialize the DictReader object
        csv_reader = csv.DictReader(file)
        
        # Loop through rows of file
        for row_number, row in enumerate(csv_reader, start=2):
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
    
    # On success add rows to json file 
    with output_json_path.open("w", encoding="utf-8") as f:
        json.dump(valid_records, f, indent=2)
    
    return valid_records, passed, failed

def create_summary(passed, failed):
    total_records = passed + failed
    print("\n\n==========[ S U M M A R Y ]==========\n\n")
    print(f"{passed}/{total_records} PASSED\n")
    print(f"{failed}/{total_records} FAILED\n")
    