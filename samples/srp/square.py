# Every software component (class, method or even a function) should have one and only one responsibility.


# The parts of the software component, Square are not closely related.
# The closeness is cohesion.
# To increase the cohesion, split up the methods.
class Square:
    def __init__(self, side):
        self.side=side
    def get_area(self):
        return self.side*self.side
    def get_perimeter(self):
        return self.side*4
    def draw(self):
        # Render a high resolution image of a square.
        pass
    def rotate(self):
        # Rotate the image of the square clockwise to
        # the required degree and re-render
        pass