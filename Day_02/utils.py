import os
import subprocess
from text_colors import COLOR_DEFAULT, COLOR_GREEN, COLOR_RED, COLOR_YELLOW

def clear_terminal():
    # Use 'cls' on Windows, 'clear' on Mac/Linux
    command = 'cls' if os.name == 'nt' else 'clear'
    
    subprocess.run(command, shell=True)

def print_result(timestamp, severity, invoice_id, vendor, message):
    match severity:
        case 'DEBUG', 'WARNING':
            print(f"{COLOR_YELLOW}{timestamp} | {severity} | {invoice_id} | {vendor} | {message}{COLOR_DEFAULT}")
        case 'INFO':
            print(f"{COLOR_GREEN}{timestamp} | {severity} | {invoice_id} | {vendor} | {message}{COLOR_DEFAULT}")
        case 'ERROR', 'CRITICAL':
            print(f"{COLOR_RED}{timestamp} | {severity} | {invoice_id} | {vendor} | {message}{COLOR_DEFAULT}")
        case _:
            print(f"{timestamp} | {severity} | {invoice_id} | {vendor} | {message}")
    