from typing import Optional

from fastapi import APIRouter, Body
from starlette.status import HTTP_200_OK, HTTP_201_CREATED

from app.api.dependencies.charge import (create_charge_dependency,
                                         get_charges_dependency)
from app.api.dependencies.refund import create_refund_dependency
from app.api.models.schemas.charge import ChargeList, ClientSecret
from app.api.models.schemas.refund import Refund

router = APIRouter()


@router.get(
    "/get_charges",
    status_code=HTTP_200_OK,
    response_model=ChargeList,
    name="GET:charges",
)
def get_charges(limit: Optional[int] = 10) -> ChargeList:
    return get_charges_dependency(limit)


@router.post(
    "/create_charge",
    status_code=HTTP_201_CREATED,
    name="POST:charge",
)
def create_charge(request_body=Body(...)) -> ClientSecret:
    return {
        "clientSecret": create_charge_dependency(
            request_body.amount, request_body.currency
        )
    }


@router.post(
    "/create_refund/{charge_id}",
    status_code=HTTP_201_CREATED,
    name="POST:refund",
)
def create_refund(charge_id: str) -> Refund:
    return create_refund_dependency(charge_id)
