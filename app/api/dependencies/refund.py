from app.services.stripe.charge import Charge


def create_refund_dependency(charge_id):
    charge = Charge()
    return charge.create_refund(charge_id)
