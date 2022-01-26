from typing import Any

from pydantic import BaseModel, Json


class Refund(BaseModel):
    id: str
    object: Any
    amount: float
    balance_transaction: Any
    charge: str
    created: str
    currency: str
    metadata: Json
    payment_intent: Any
    reason: Any
    receipt_number: Any
    source_transfer_reversal: Any
    status: str
    transfer_reversal: Any
