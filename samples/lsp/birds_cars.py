# Objects must be replacable with their subtypes without affecting the correctness of the program.


class Bird():
    def fly(self):
        # Fly High!
        print("Birds Fly!")

# Design Flaw, Prone for Errors/Bugs and voilates LSP.
class Ostrich(Bird):
    def run(self):
        print("I can run!")
    def fly(self):
        # Can't implement this method!
        pass

o1=Ostrich()
# voilation of Liskov Principle
o1.fly()

class Car():
    def get_cabin_width(self):
        # return Cabin width
        print("Car's Have Cabin Width!")

class RacingCar(Car):
    def get_cockpit_width(self):
        # return cockpit width
        print("I can give you my CockPit Width.")
    def get_cabin_width(self):
        # Can't implement this method
        pass

# No results are produced because the methods are not implemented.
# the sub-types are not able to replace the objects.
# This clearly calls for increasing the level of abstraction.
c1=Car()
c2=Car()
r1=RacingCar()

cars=[c1,c2,r1]
for car in cars:
    car.get_cabin_width()