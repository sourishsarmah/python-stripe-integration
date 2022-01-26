import stripe

from app.core.config import STRIPE_SECRET_KEY


class Charge:
    def __init__(self) -> None:
        stripe.api_key = STRIPE_SECRET_KEY
        self.__stripe = stripe

    def create_charge(self, amount, currency="usd", description=None) -> str:
        pi = self.__stripe.PaymentIntent.create(
            amount=amount,
            currency=currency,
            description=description,
            automatic_payment_methods={
                "enabled": True,
            },
        )
        return pi["client_secret"]

    def get_charge_list(self, limit=10):
        return self.__stripe.Charge.list(limit=limit)

    def create_refund(self, charge_id):
        return self.__stripe.Refund.create(charge=charge_id)
