from validator.processor import process_purchase_orders, create_summary
from validator.logging_config import configure_logger
from validator.paths import INPUT_CSV, OUTPUT_JSON, ERROR_LOG

def main():
    configure_logger(ERROR_LOG)
    _, passed, failed = process_purchase_orders(INPUT_CSV, OUTPUT_JSON)
    create_summary(passed, failed)
    
if __name__ == '__main__':
    main()