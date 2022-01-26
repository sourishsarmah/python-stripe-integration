from app.services.stripe.charge import Charge


def get_charges_dependency(limit):
    charge = Charge()
    return charge.get_charge_list(limit)


def create_charge_dependency(amount, currency, description=None):
    charge = Charge()
    return charge.create_charge(amount, currency, description=description)
