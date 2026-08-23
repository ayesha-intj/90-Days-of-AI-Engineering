from pydantic import BaseModel, Field
from decimal import Decimal
from datetime import datetime

class PurchaseOrderModel(BaseModel):
    po_id: str
    vendor: str
    amount: Decimal = Field(gt=0)
    currency: str
    submitted_at: datetime
    