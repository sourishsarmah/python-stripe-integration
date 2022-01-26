from typing import Optional

from fastapi import APIRouter
from starlette.status import HTTP_200_OK

from app.api.dependencies.charge import get_charges_dependency
from app.api.models.schemas.charge import ChargeList

router = APIRouter()


@router.get(
    "/get_charges",
    status_code=HTTP_200_OK,
    response_model=ChargeList,
    name="GET:charges",
)
def get_charges(limit: Optional[int] = 10) -> ChargeList:
    return get_charges_dependency(limit)
