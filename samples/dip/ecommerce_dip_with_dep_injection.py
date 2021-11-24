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

# To have the depency injected, create a constructor for the ProductCatalog so that
# this high level module doesn't have to worry about instantiating a lower level class.
# Whoever wants to use the high level module will call it and inject dependencies into
# it during the run time.
class ProductCatalog:
    def __init__(self, ProductRepositoryObj):
        self.product_rep_obj = ProductRepositoryObj
    def list_all_products(self):
        return self.product_rep_obj.get_all_product_names()

if __name__ == "__main__":
    product_repository_object=ProductFactory.create()
    PC=ProductCatalog(product_repository_object)
    print(PC.list_all_products())