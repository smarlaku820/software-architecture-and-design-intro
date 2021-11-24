from abc import ABC, abstractmethod

"""ABS Classes Usage: We use abstract classes when there are some common features that needs to be shared by all the objects 
   that are derived from the abstract class. (or child class)
   Interfaces: An Interface in Python is nothing but its an Abstract class which contains only Abstract methods.
   We use interface when all features needs to be implemented differently for different objects.
    Note:- We cannot create objects of an Interface/Abstract class. 
           Interfaces Standardize the Behaviour.
           Abstract classes generalizes the Behaviour
"""
class DefenceForces(ABC):
    @abstractmethod
    def Area(self):
        pass
    def Guns(self):
        return "AK47"

class Army(DefenceForces):
    def Area(self):
        return "Land"

class Navy(DefenceForces):
    def Area(self):
        return "Sea"

class AirForce(DefenceForces):
    def Area(self):
        return "Skies"