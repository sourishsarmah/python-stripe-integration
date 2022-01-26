from app.services.stripe.charge import StripeCharge


def create_refund_dependency(charge_id):
    charge = StripeCharge()
    return charge.create_refund(charge_id)
