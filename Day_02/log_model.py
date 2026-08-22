from dataclasses import dataclass
from datetime import datetime

@dataclass
class LogEntry:
    timestamp: datetime
    severity: str
    invoice_id: str
    vendor: str
    message: str
    
    def __repr__(self):
        return f"LogEntry(timestamp={self.timestamp}, severity={self.severity}, invoice id={self.invoice_id}, vendor = {self.vendor}, msg={self.message})"