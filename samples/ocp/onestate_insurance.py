# Software components must be closed for modification and open for extension.

# What happens if the OneState Insurance company wants to provide for Home Insurance and in future
# there are prospects for selling Travel Insurance too.
# Do we have to keep modifying our Insurance Premium Discount Calculator class ?
# Clearly a voilation of OCP (Open Closed Principle)

class InsurancePremiumDiscountCalculator:
    def __init__(self):
        pass

    def get_discount_health_premium_percent(HealthInsuranceCustomer):
        if HealthInsuranceCustomer.isLoyal():
            return 20
        else:
            return 0

    def get_discount_vehicle_premium_precent(VehicleInsuranceCustomer):
        if VehicleInsuranceCustomer.isLoyal():
            return 20
        else:
            return 0


class HealthInsuranceCustomer:
    def __init__(self):
        pass

    def isLoyal(self):
        # based on some evaulations, True or False will be returned.
        return True # or False

class VehicleInsuranceCustomer:
    def __init__(self):
        pass

    def isLoyal(self):
        # based on some evaulations, True or False will be returned.
        return True # or False