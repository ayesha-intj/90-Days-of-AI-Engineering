import logging
import random
from datetime import datetime
from collections import Counter
from logging.handlers import RotatingFileHandler
from log_config import LogLevel, MessageType, MESSAGES 

def run_audit():
    # Generate 200-lines mock corporate server log
    with open("Day_01/server.log", "w") as file:
        for _ in range(1, 201):
            now = datetime.now()
            timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
                
            chosen_message_type = random.choice(list(MESSAGES))
            chosen_log_level = random.choice(list(MESSAGES[chosen_message_type]))
            chosen_message = random.choice(list(MESSAGES[chosen_message_type.value][chosen_log_level.value]))
                
            result_row = f"{timestamp} | {chosen_log_level.value} | {chosen_message_type.value.upper()} | {chosen_message}\n"
            file.write(result_row)
                 
            pass
            
    # Configure the basic logging module
    logger = logging.getLogger("AuditLogger")
    logger.setLevel(logging.DEBUG)
    layout_format = logging.Formatter("%(asctime)s | %(levelname)-8s | %(name)s | %(message)s")

    # Attach Stream Handler
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(layout_format)
    logger.addHandler(stream_handler)
    
    # Attach rotating file handler (analysis.log)
    rotating_file_handler = RotatingFileHandler("Day_01/analysis.log", maxBytes=50000, backupCount=2)
    rotating_file_handler.setLevel(logging.DEBUG)
    
    # Clean up formatting for analysis.log rows
    analysis_file_format = logging.Formatter("%(message)s")
    rotating_file_handler.setFormatter(analysis_file_format)
    logger.addHandler(rotating_file_handler)

    # A terminal logger that only points to the terminal stream handler
    terminal_logger = logging.getLogger("TerminalSummary")
    terminal_logger.setLevel(logging.INFO)
    terminal_logger.addHandler(stream_handler)
    
    # Prevents messages from leaking to other loggers
    terminal_logger.propagate = False  

    # Open server.log and iterate it line by line with split each line on | 
    severity_counter = Counter()

    # Open server.log and iterate it line by line
    with open("Day_01/server.log", "r") as file:
        for line in file:
            raw_parts = line.split("|")
            clean_parts = [part.strip() for part in raw_parts]
            log_time, severity, msg_type, message = clean_parts
            
            # Increment the counter for the current line's severity
            severity_counter[severity] += 1
            
            # Build the ACTUAL log content from the file row
            log_content = f"{log_time} | {severity} | {msg_type.upper()} | {message}"
            
            # Match-case routes the ACTUAL message into analysis.log line-by-line
            match severity:
                case "DEBUG":
                    logger.debug(log_content)
                case "INFO":
                    logger.info(log_content)
                case "WARNING":
                    logger.warning(log_content)
                case "ERROR":
                    logger.error(log_content)
                case "CRITICAL":
                    logger.critical(log_content)
                case _:
                    logger.warning(f"Unknown severity level encountered: {severity}")
    
    # Clear the layout prefix elements before displaying metrics summary
    clean_terminal_format = logging.Formatter("%(message)s")
    stream_handler.setFormatter(clean_terminal_format)

    terminal_logger.info("\n--- Severity Running Tally Metrics ---")

    # Final Output String
    formatted_tally = (
        f"DEBUG: {severity_counter['DEBUG']} | "
        f"INFO: {severity_counter['INFO']} | "
        f"WARNING: {severity_counter['WARNING']} | "
        f"ERROR: {severity_counter['ERROR']} | "
        f"CRITICAL: {severity_counter['CRITICAL']}"
    )
    
    terminal_logger.info(formatted_tally)

if __name__ == '__main__':
    run_audit()
