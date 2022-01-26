import requests
import stripe
from stripe import Charge, PaymentIntent, PaymentMethod

from app.core.config import STRIPE_SECRET_KEY


class StripeCharge:

    api_key = STRIPE_SECRET_KEY

    def __create_payment_method(self, card) -> PaymentMethod:
        pm = PaymentMethod.create(type="card", card=dict(card), api_key=self.api_key)
        return pm

    def create_charge(self, amount, card, currency="inr", description=None) -> str:
        pi = PaymentIntent.create(
            amount=amount,
            currency=currency,
            description=description,
            capture_method="manual",
            api_key=self.api_key,
        )

        ps = self.__create_payment_method(card)

        pi = stripe.PaymentIntent.confirm(
            pi["id"], payment_method=ps, api_key=self.api_key
        )

        url = pi["next_action"]["use_stripe_sdk"]["stripe_js"]

        requests.get(url)

        charge = Charge.list(limit=1, api_key=self.api_key).get("data")[0]

        return charge

    def capture_charge(self, charge_id):
        charge = Charge.retrieve(charge_id, api_key=self.api_key)
        pi = PaymentIntent.capture(charge["payment_intent"], api_key=self.api_key)
        return pi["charges"]["data"][0]

    def get_charge_list(self, limit=10):
        return Charge.list(limit=limit, api_key=self.api_key)
