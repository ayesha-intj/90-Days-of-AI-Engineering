from validator.processor import process_purchase_orders, create_summary

def main():
    _, passed, failed = process_purchase_orders()
    create_summary(passed, failed)
    
if __name__ == '__main__':
    main()