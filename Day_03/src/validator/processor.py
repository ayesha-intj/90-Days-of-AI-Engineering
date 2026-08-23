import csv
import logging
from pydantic import ValidationError
from validator import PurchaseOrderModel

def process_purchase_orders():
    file_path = "Day_03/data/input/purchase_orders_raw.csv"
    
    # Open purchase_orders_raw CSV file
    with open(file_path, mode="r") as file:
        # Initialize the DictReader object
        csv_reader = csv.DictReader(file)
        
        
        # Loop through rows of file
        for row in csv_reader:
            try:
                print(row)
                # On success add rows to json file 
                
                # Track counts for final pass/fail ratio
                
            except ValidationError as exc:
                # On failure record the row number and show error
                print("")
                
                # Track counts for final pass/fail ratio