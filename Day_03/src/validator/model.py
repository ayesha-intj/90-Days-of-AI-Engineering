from pydantic import BaseModel, Field
from decimal import Decimal
from datetime import datetime

class PurchaseOrderModel(BaseModel):
    po_id: str = Field(min_length=1)
    vendor: str = Field(min_length=1)
    amount: Decimal = Field(gt=0)
    currency: str = Field(min_length=1)
    submitted_at: datetime = Field() 
    