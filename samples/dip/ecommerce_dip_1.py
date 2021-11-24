from abc import ABC, abstractmethod

class ProductRepository(ABC):
    @abstractmethod
    def get_all_product_names():
        pass

# The Low-Level Module depends on a Product Interface.
# This dependency on the high-level module is reversed, this is called dependency inversion principle.
class SQLProductRepository(ProductRepository):
    def get_all_product_names(self):
        return ["clothes","electronics","groceries"]

class ProductFactory:
    @staticmethod
    def create():
        return SQLProductRepository()

# The High level module now depends on abstractions.
class ProductCatalog:
    def list_all_products(self):
        return ProductFactory.create().get_all_product_names()

pc=ProductCatalog()
print(pc.list_all_products())