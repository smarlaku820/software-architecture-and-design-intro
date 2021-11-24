# Dependency Inversion Principle:
# High level modules should not depend on Low level modules. Both should depend on abstractions.
# Abstractions should not depend on details and details must depend on abstractions.

# ProductCatalog [HighLevel Module] depends on the SQLProductRepository [LowLevel Module]
class ProductCatalog:
    def list_all_products(self):
        spr=SQLProductRepository()
        return spr.get_all_product_names()

class SQLProductRepository:
    def get_all_product_names(self):
        return ["clothes","electronics","groceries"]

pc=ProductCatalog()
print(pc.list_all_products())