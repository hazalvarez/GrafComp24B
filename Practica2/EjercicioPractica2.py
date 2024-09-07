from manim import *
class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PURPLE, opacity=0.5).shift(2 * UP+4*RIGHT)  # set the color and transparency
        circle1 = Circle()  # create a circle
        circle1.set_fill(BLUE, opacity=0.5).shift(2 * DOWN+4*LEFT)  # set the color and transparency
        square = Square()  # create a square
        square.set_fill(WHITE, opacity=0.5).shift(4 * RIGHT+2*DOWN)  # set the color and transparency
        square1 = Square()  # create a square
        square1.set_fill(RED, opacity=1).shift(4 * LEFT+2*UP)  # set the color and transparency  
        self.play(Create(circle1), Create(square),Create(circle), Create(square1))  # show the shapes on screen
        
        