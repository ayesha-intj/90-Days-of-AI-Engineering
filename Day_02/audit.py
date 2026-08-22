from datetime import datetime
import random
from log_config import LogLevel, MessageCategory, MESSAGES, VENDORS

def run_audit():
    # produce invoice_queue.log, a 200-line mock invoice-processing-queue log 
    with open("Day_02/invoice_queue.log", "w") as file:
        for i in range(1, 201):
            now = datetime.now()
            timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
                            
            chosen_message_category = random.choice(list(MESSAGES))
            chosen_log_level = random.choice(list(MESSAGES[chosen_message_category]))
            chosen_message = random.choice(list(MESSAGES[chosen_message_category.value][chosen_log_level.value]))
            invoice_id = i
            vendor = random.choice(VENDORS)
            result_row = f"{timestamp} | {chosen_log_level.value} | INV-{invoice_id} | {vendor} | {chosen_message}\n"
            file.write(result_row)
                             
            pass
    
if __name__ == '__main__':
    run_audit()