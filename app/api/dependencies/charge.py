from app.services.stripe.charge import Charge


def get_charges_dependency(limit):
    charge = Charge()
    return charge.get_charge_list(limit)
