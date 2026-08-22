from log_model import LogEntry
import utils
from collections import Counter
from text_colors import COLOR_GREEN, COLOR_DEFAULT

# Define a LogAuditor class
class LogAuditor:
    # Add Constructor
    def __init__(self):
        self.log_entries: list[LogEntry] = []
    
    # Create method 1 - load(path)
    def load(self, path):
        with open(path, "r") as file:
            for line in file:
                raw_parts = line.split("|")
                clean_parts = [part.strip() for part in raw_parts]
                inv_timestamp, inv_severity, inv_id, inv_vendor, inv_message = clean_parts
                entry = LogEntry(
                    timestamp = inv_timestamp,
                    severity = inv_severity,
                    invoice_id = inv_id,
                    vendor = inv_vendor,
                    message = inv_message,
                )
                
                self.log_entries.append(entry)
    
    # Create method 2 - filter_by_severity(level)
    def filter_by_severity(self, level):
        filtered_list = [e for e in self.log_entries if e.severity == level]
        for entry in filtered_list:
            utils.print_result(
            entry.timestamp, 
            entry.severity, 
            entry.invoice_id, 
            entry.vendor, 
            entry.message
            )
    
    # Create method 3 - summarize()
    def summarize(self):
        vendor_count = Counter()
        severity_count = Counter()
        for entry in self.log_entries:
            vendor_count[entry.vendor]+=1
            severity_count[entry.severity]+=1
            
        for item, count in vendor_count.items():
            print(f"{item}: {count}")
        
        print("=====================")
        for item, count in severity_count.items():
            print(f"{item}: {count}")
                
    # Create __repr__ method
    def __repr__(self):
        return f"{COLOR_GREEN}SUCCESS: Data Added into List{COLOR_DEFAULT}"