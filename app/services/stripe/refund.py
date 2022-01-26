from stripe import Refund

from app.core.config import STRIPE_SECRET_KEY


class StripeRefund:

    api_key = STRIPE_SECRET_KEY

    def create_refund(self, charge_id) -> Refund:
        return Refund.create(charge=charge_id, api_key=self.api_key)
