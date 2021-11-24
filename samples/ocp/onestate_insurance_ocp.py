# Software components must be closed for modification and open for extension.

from abc import ABC, abstractmethod

class InsurancePremiumDiscountCalculator:
    def __init__(self):
        pass
    def get_discount_health_premium_percent(self, customer):
        if customer.isLoyal():
            return 20
        else:
            return 0

# An interface (API) that must be implemented by different types of insurance objects.
# Customer Interface providing standards as to what needs to be implemented.
class Customer(ABC):
    @abstractmethod
    def isLoyalCustomer(self) -> bool:
        pass

# Extending the Customer Class or Deriving from the customer class.
class HealthInsuranceCustomer(Customer):
    # Implementing isLoyalCustomer for Health Insurance Customers.
    def isLoyalCustomer(self):
        # based on some evaulations, True or False will be returned.
        return True # or False

class VehicleInsuranceCustomer(Customer):
    # Implementing isLoyalCustomer for Vehicle Insurance Customers.
    def isLoyalCustomer(self):
        # based on some evaulations, True or False will be returned.
        return True # or False