# Objects can be substituted with their subtypes without worrying about the correctness of the program.
class Product:
    discount=20
    def __init__(self):
        pass
    def get_discount(self):
        return self.discount


class InHouseProduct(Product):
    def get_discount(self):
        return self.apply_extra_discount()
    def apply_extra_discount(self):
        return 1.5*(super().discount)

p1=Product()
p2=Product()
p3=InHouseProduct()

# Now, in this case when we are iterating through this module
# we just have to tell that the list of products are all an extension of the product class
# And we just call the get_discount() method and automatically everything is taken care off.
products=[p1, p2, p3]
for product in products:
    print(product.get_discount())