# Objects can be substituted with their subtypes without worrying about the correctness of the program.
class Product:
    discount=20
    def __init__(self):
        pass
    def get_discount(self):
        return self.discount

# Poor Design when creating sub-classes (extending another class).
# If you cannot create a sub-class or a child class where it cannot be replaced, then you need to
# go for higher level of abstraction and make sure such class can completely replace the base class.
class InHouseProduct(Product):
    # doesn't override the get_discount method, but provides discount differently.
    def apply_extra_discount(self):
        return 1.5*(super().discount)

p1=Product()
p2=Product()
p3=InHouseProduct()

# We ask if the product type is a particular type of object.
# clearly voilates LSP: Tell, Don't Ask.
products=[p1, p2, p3]
for product in products:
    if isinstance(product,InHouseProduct):
        print(product.apply_extra_discount())
    else:
        print(product.get_discount())