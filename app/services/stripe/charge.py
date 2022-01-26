import stripe

from app.core.config import STRIPE_SECRET_KEY


class Charge:
    def __init__(self) -> None:
        stripe.api_key = STRIPE_SECRET_KEY
        self.__charge = stripe.Charge()

    def get_charge_list(self, limit=10):
        return self.__charge.list(limit=limit)
