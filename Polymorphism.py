from math import pi
class Shape:
    def draw(self):
        # Draw Code
        class circle(Shape):
            radius_cm = 4
            origin = (0,0)
            def  draw(self):
            #Draw Circumference at origin
                Circumference = pi * (self.radius_cm ** 2)
