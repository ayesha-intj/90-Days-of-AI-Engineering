from enum import StrEnum

class LogLevel(StrEnum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"

class MessageCategory(StrEnum):
    QUEUE = "QUEUE"
    VALIDATION = "VALIDATION"
    PROCESSING = "PROCESSING"

MESSAGES = {
    MessageCategory.QUEUE: {
        LogLevel.DEBUG: [
            "Polling queue table for next batch of pending invoice records",
            "Checking message broker connection heartbeat status",
            "Reading queue partition offset markers from disk",
            "Allocating temporary memory buffer for incoming payload batch",
            "Inspecting consumer group lag metrics for queue backlog"
        ],
        LogLevel.INFO: [
            "Successfully fetched batch of 10 pending invoice tasks from queue",
            "Invoice item successfully acknowledged and removed from active queue",
            "Queue consumer thread pool scaled up to match traffic load",
            "Batch processing cycle completed with zero remaining items",
            "Queue connection re-established successfully after brief idle"
        ],
        LogLevel.WARNING: [
            "Queue processing latency exceeding optimal threshold limits",
            "High backlog detected in invoice queue partition 2",
            "Consumer heartbeat delayed due to network congestion",
            "Queue message retention period approaching expiration window",
            "Duplicate delivery flag detected on incoming queue item"
        ],
        LogLevel.ERROR: [
            "Failed to acknowledge processed invoice item in queue registry",
            "Queue connection lost during batch fetch operation",
            "Malformed message payload received from broker channel",
            "Transaction rollback triggered due to queue dispatch timeout",
            "Failed to commit consumer offset position to storage"
        ],
        LogLevel.CRITICAL: [
            "Invoice message broker cluster completely unreachable",
            "Fatal memory exhaustion while buffering high-volume queue batch",
            "Persistent queue storage corruption detected on primary node",
            "Dead-letter queue fully saturated with failed invoice items",
            "Complete deadlock encountered across all queue consumer threads"
        ]
    },
    MessageCategory.VALIDATION: {
        LogLevel.DEBUG: [
            "Parsing XML invoice payload against schema definition",
            "Extracting line-item quantities and unit prices for checks",
            "Validating vendor tax ID format structure and length",
            "Checking purchase order reference number against local cache",
            "Inspecting currency code compliance for vendor profile"
        ],
        LogLevel.INFO: [
            "Invoice schema validation passed successfully for record",
            "Vendor identity verified against authorized supplier database",
            "Tax calculation check completed with matching line totals",
            "Purchase order reference matched successfully in system",
            "Invoice line items verified and cleared for processing"
        ],
        LogLevel.WARNING: [
            "Vendor tax ID format is deprecated, proceeding with warning",
            "Invoice amount exceeds typical threshold for this vendor",
            "Minor discrepancy found between subtotal and sum of line items",
            "Purchase order reference expiring within current billing cycle",
            "Missing optional metadata field in incoming invoice payload"
        ],
        LogLevel.ERROR: [
            "Invoice schema validation failed due to missing mandatory fields",
            "Vendor authorization check failed against active supplier list",
            "Line item total calculation mismatch detected during validation",
            "Unrecognized currency code provided in invoice header",
            "Failed to parse timestamp format within invoice metadata"
        ],
        LogLevel.CRITICAL: [
            "Validation rule engine crashed due to missing core dependency",
            "Supplier database lookup completely failed during validation sequence",
            "Critical schema definition file missing from execution directory",
            "Unrecoverable memory fault during deep payload inspection",
            "Security sanitization check failed with severe structural error"
        ]
    },
    MessageCategory.PROCESSING: {
        LogLevel.DEBUG: [
            "Initiating ledger write sequence for validated invoice record",
            "Formatting invoice data payload for downstream ERP integration",
            "Checking database connection pool availability for insert",
            "Evaluating discount application rules for line items",
            "Inspecting transaction isolation level for ledger commit"
        ],
        LogLevel.INFO: [
            "Invoice successfully processed and recorded in ledger system",
            "Digital purchase receipt dispatched to vendor contact email",
            "Payment scheduling pipeline updated with new invoice entry",
            "Ledger commit completed successfully for current batch",
            "ERP synchronization hook executed without errors"
        ],
        LogLevel.WARNING: [
            "Ledger write operation took longer than expected execution window",
            "Downstream ERP integration endpoint returned slow response",
            "Automatic retry triggered for transient ledger insertion failure",
            "Vendor notification dispatch delayed by email queue backup",
            "Partial allocation applied to invoice due to remaining balance"
        ],
        LogLevel.ERROR: [
            "Database timeout while attempting to write invoice record",
            "Failed to update invoice settlement status in financial ledger",
            "Downstream ERP integration service rejected payload structure",
            "Transaction commit aborted due to concurrency conflict",
            "Failed to dispatch vendor confirmation notification email"
        ],
        LogLevel.CRITICAL: [
            "Financial ledger database balance variance detected instantly",
            "Total system failure during final invoice state transition",
            "Core payment tracking module dropped completely offline",
            "Encryption module failure while saving sensitive invoice fields",
            "Catastrophic storage write failure during ledger commit phase"
        ]
    }
}

VENDORS = [
    "Office Supplies Co.", "Cloud Services Inc.", "Logistics Global", 
    "Hardware Depot", "Marketing Agency", "Enterprise Solutions", "SaaSify LLC"
]