from manim import *

class LineAnimation2(Scene):
    def construct(self):
        step1 = Text("Step 1")
        step2 = Text("Step 2")
        step1.move_to(LEFT * 2 + DOWN * 2)
        step2.move_to(RIGHT * 4 + UP * 2)
        line = Line(step1.get_right(), step2.get_left(), buff=0.1)
        self.play(Write(step1), Write(step2))
        self.play(GrowFromPoint(line, step1.get_right()))
        new_position = step2.get_center() + LEFT * 2
        self.play(step2.animate.move_to(new_position), run_time=2)
        updated_line = Line(step1.get_right(), step2.get_left(), buff=0.1)
        self.play(Transform(line, updated_line))
        self.wait()
