import stripe

from app.core.config import STRIPE_SECRET_KEY


class Charge:
    def __init__(self) -> None:
        stripe.api_key = STRIPE_SECRET_KEY
        self.__paymentintent = stripe.PaymentIntent()
        self.__charge = stripe.Charge()

    def create_charge(self, amount, currency="usd", description=None) -> str:
        pi = self.__paymentintent.create(
            amount=amount,
            currency=currency,
            description=description,
            automatic_payment_methods={
                "enabled": True,
            },
        )
        return pi["client_secret"]

    def get_charge_list(self, limit=10):
        return self.__charge.list(limit=limit)
