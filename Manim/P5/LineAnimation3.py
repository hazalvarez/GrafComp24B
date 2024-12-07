from manim import *

class LineAnimation3(Scene):
    def construct(self):
        step1 = Text("Step 1")
        step2 = Text("Step 2")
        step3 = step2.copy()
        step1.move_to(LEFT * 2 + DOWN * 2)
        step2.move_to(RIGHT * 4 + UP * 2)
        step3.next_to(step2, LEFT * 2)
        line = Line(step1.get_right(), step2.get_left(), buff=0.1)
        lineCopy = Line(step1.get_right(), step3.get_bottom(), buff=0.1)
        self.play(Write(step1), Write(step2))
        self.play(GrowFromPoint(line, step1.get_right()))
        self.play(
            ReplacementTransform(step2, step3),
            ReplacementTransform(line, lineCopy)
        )
        self.wait()
