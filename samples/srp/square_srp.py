# Every software component (class, method or even a function) should have one and only one responsibility.

# get_area and get_perimeter
class Square:
    def __init__(self, side):
        self.side=side
    def get_area(self):
        return self.side*self.side
    def get_perimeter(self):
        return self.side*4

# draw & rotate work with the graphical aspects of rendering the square.
class SquareUI:
    def __init__(self):
        pass
    def draw(self):
        # Render a high resolution image of a square.
        pass
    def rotate(self):
        # Rotate the image of the square clockwise to
        # the required degree and re-render
        pass