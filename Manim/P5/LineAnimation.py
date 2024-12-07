from manim import *
class LineAnimation(Scene):
    def construct(self):
        step1 = Text("Step 1")
        step2 = Text("Step 2")
        step1.move_to(LEFT*2+DOWN*2)
        step2.move_to(4*RIGHT+2*UP)
        arrow1 = Line(step1.get_right(),step2.get_left(),buff=0.1)
        arrow1.set_color(RED)
        arrow2 = Line(step1.get_top(),step2.get_bottom(),buff=0.1)
        arrow2.set_color(BLUE)
        self.play(Write(step1),Write(step2))
        self.play(Create(arrow1))
        self.play(Create(arrow2))
        self.wait()
