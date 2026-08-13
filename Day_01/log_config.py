from enum import StrEnum

class LogLevel(StrEnum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"

class MessageType(StrEnum):
    AUTH = "AUTH"
    PAYMENTS = "PAYMENTS"
    DATABASE = "DATABASE"

MESSAGES = {
    MessageType.AUTH: {
        LogLevel.DEBUG: [
            "Parsing token claims from incoming request header",
            "Validating password hash complexity requirements",
            "Checking active session storage cache keys",
            "Evaluating attribute-based access control policies",
            "Reading oauth client configuration from disk",
            "Inspecting refresh token expiration properties",
            "Checking multifactor token delivery parameters",
            "Extracting user metadata from authentication payload",
            "Verifying security signature against local keys",
            "Inspecting cross-origin request origin domain"
        ],
        LogLevel.INFO: [
            "User successfully signed in from verified device",
            "New user account registration form processed",
            "Password reset request initiated by account owner",
            "Multifactor authentication challenge successfully completed",
            "User session cleanly terminated via logout endpoint",
            "API authentication key refreshed by client",
            "Account email address updated successfully",
            "Security verification answers successfully registered",
            "User profile synchronization with identity provider finished",
            "Temporary login verification code dispatched to device"
        ],
        LogLevel.WARNING: [
            "Failed login attempt registered for non-existent user",
            "Password validation threshold approaching account suspension",
            "Expired authentication token presented to private endpoint",
            "Login attempt detected from unverified geographic location",
            "Session validation check running slower than timeout margins",
            "Unsecured connection protocol used for authentication route",
            "User password age exceeding recommended security interval",
            "Authentication verification code requested multiple times quickly",
            "Deprecate endpoint version accessed during login sequence",
            "Account access pattern matching automated script behavior"
        ],
        LogLevel.ERROR: [
            "Invalid authorization token signature structure provided",
            "External identity provider connection returned bad state",
            "Account locked due to excessive authentication failures",
            "Cryptographic decryption operation failed on secure token",
            "User validation framework failed to parse request format",
            "Cross-site request forgery handshake validation failed",
            "MFA delivery service rejected target destination address",
            "Permission database lookup timed out during checking",
            "Token generation algorithm missing required environment variable",
            "Authentication state cache synchronization failed completely"
        ],
        LogLevel.CRITICAL: [
            "Authentication database connection pool fully exhausted",
            "Private signing key file missing from configuration directory",
            "Brute force credential stuffing attack currently active",
            "Authorization system bypass pattern detected on core logic",
            "Encryption module failed to initialize secure random generator",
            "Identity provider cluster reported total cluster outage",
            "Security validation middleware completely skipped via misconfiguration",
            "User privilege escalation exploit attempt detected on endpoint",
            "Session revocation registry unavailable to match validation requests",
            "Critical certificate authority expiration causing login failure"
        ]
    },
    MessageType.PAYMENTS: {
        LogLevel.DEBUG: [
            "Checking payment processor gateway endpoint state",
            "Formatting currency numeric value to matching format",
            "Inspecting local transaction sequence allocation reference",
            "Extracting payment method metadata from request data",
            "Calculating applicable regional processing surcharge matrix",
            "Checking idempotency key existence in transactional registry",
            "Verifying webhook routing signature with processor keys",
            "Inspecting currency exchange conversion evaluation metrics",
            "Reading discount coupon calculation rule rules file",
            "Validating payload schema structure for gateway delivery"
        ],
        LogLevel.INFO: [
            "Transaction processed successfully through processor gateway",
            "Invoice record generated and assigned identifier code",
            "Subscription renewal pipeline updated for active client",
            "Refund allocation operation completed for requested item",
            "Payment method mapping successfully added to profile",
            "Digital purchase receipt dispatched via message queue",
            "Bank settlement file exported to scheduled directory",
            "Promotion code applied to active checkout process",
            "Payer account validation verification check passed completely",
            "Partial allocation payment accepted for outstanding record"
        ],
        LogLevel.WARNING: [
            "Gateway communication latency exceeding optimal target window",
            "Payment authorization request returned retry status response",
            "Card expiration date approaching within current month",
            "Transaction value exceeding typical single account threshold",
            "Processor webhook delivered multiple times for same item",
            "Currency conversion rate fluctuation exceeds standard buffer",
            "Card validation digit mismatch flag returned from check",
            "Billing address lookup returned incomplete location match",
            "Automated subscription retry pipeline delayed by queue backup",
            "Discount code match found but item eligibility criteria failed"
        ],
        LogLevel.ERROR: [
            "Transaction declined by issuing financial branch location",
            "Gateway handshake rejected due to invalid merchant credentials",
            "Idempotency token conflict encountered during charge request",
            "Payment processing bridge returned malformed data format",
            "Refund request rejected due to insufficient processing reserves",
            "Secure ledger entry validation mismatch during calculation",
            "Processor interface returned undocumented error response code",
            "Tax evaluation service dropped connection during computation",
            "Card processing pipeline encountered serialization blocking failure",
            "Failed to update invoice settlement status in ledger"
        ],
        LogLevel.CRITICAL: [
            "Payment processing gateway down or unreachable globally",
            "Financial database ledger balance variance detected instantly",
            "Encryption failure encountered during card tokenization route",
            "Payment webhook endpoint processing total timeout lockup",
            "PCI compliance logging server stopped accepting secure feeds",
            "Automated corporate payout script failed midway through routine",
            "Fraud detection evaluation engine dropped completely offline",
            "Merchant banking distribution file corrupted during assembly",
            "Decryption keys for payment data storage lost or unreadable",
            "Duplicate charging event loop detected running on subscriptions"
        ]
    },
    MessageType.DATABASE: {
        LogLevel.DEBUG: [
            "Compiling raw SQL string from builder pattern",
            "Checking internal buffer pool index tracking slots",
            "Inspecting execution cost value for query analyzer",
            "Evaluating write ahead log file segment markers",
            "Reading table metadata block from storage file",
            "Verifying internal isolation level settings for session",
            "Checking read replica network communication latency values",
            "Parsing database driver environment parameters array",
            "Inspecting lock hierarchy structure for target resource",
            "Analyzing column index cardinality for optimal path selection"
        ],
        LogLevel.INFO: [
            "Database connection pool successfully initialized and ready",
            "Scheduled database backup file safely stored remotely",
            "Migration script sequence executed cleanly on schema",
            "Index optimization routine completed for system tables",
            "Read replica node caught up with master pipeline",
            "Database engine stats gathered and internal caches cleared",
            "Vacuum cleanup script recovered unused disk blocks",
            "Historical archive data dropped cleanly from active table",
            "Connection monitoring check returned healthy system status",
            "Configuration file reload completed without dropping sessions"
        ],
        LogLevel.WARNING: [
            "Query processing time exceeded standard performance threshold",
            "Active connection allocation reaching maximum pool capacity",
            "Deadlock hazard encountered and handled via automatic retry",
            "Storage volume partition space dipping below safety line",
            "Replica duplication gap widening beyond acceptable interval",
            "Table scanning operation triggered due to missing index",
        ]
    }
}