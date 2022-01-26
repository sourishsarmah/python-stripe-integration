from typing import Any, List

from pydantic import BaseModel
from pydantic.json import UUID


class Charge(BaseModel):
    charge_id: UUID


class ChargeList(BaseModel):
    data: List[Any]
    has_more: bool
