

# Increasing the level of abstraction by defining the vehicle class
# And overriding the get_interior_width in the sub-classes.
# Hierarchy Breaking for getting the LSP principle upheld.
class Vehicle:
    def __init__(self) -> None:
        pass
    def get_manufactuere(self):
        pass
    def get_make(self):
        pass
    def seating_capacity(self):
        pass
    def get_interior_width(self):
        print("Vehicle!")

class Car(Vehicle):
    # Extending vehicle class and overriding the methods.
    def get_interior_width(self):
        return self.get_cabin_width()
    def get_cabin_width(self):
        print("Cars Have Cabin, Here is my Cabin Width")

class RacingCar(Vehicle):
    # Extending vehicle class and overriding the methods.
    def get_interior_width(self):
        return self.get_cockpit_width()
    def get_cockpit_width(self):
        print("Racing Cars have CockPit, Here is I my CockPit!")

c1=Car()
c2=Car()
r1=RacingCar()

cars=[c1,c2,r1]
for car in cars:
    car.get_interior_width()