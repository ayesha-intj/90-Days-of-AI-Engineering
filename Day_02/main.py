import audit
import time
import log_auditor as la
import argparse
from text_colors import COLOR_YELLOW, COLOR_DEFAULT

audit.run_audit()
auditor_obj = la.LogAuditor()
print(f"{COLOR_YELLOW}Loading Invoice Queue and Adding to List...{COLOR_DEFAULT}")
time.sleep(1)
print(auditor_obj)
auditor_obj.load("Day_02/invoice_queue.log")
time.sleep(1)

 # Accept a command-line flag, e.g. --severity ERROR
parser = argparse.ArgumentParser()
parser.add_argument("--severity")
args = parser.parse_args()

if args.severity:
    print(f"\n{COLOR_YELLOW}--- Filtered Results for {args.severity} ---{COLOR_DEFAULT}")
    auditor_obj.filter_by_severity(args.severity.upper())
else:
    print(f"\n{COLOR_YELLOW}--- Summary ---{COLOR_DEFAULT}")
    auditor_obj.summarize()