from manim import *
class Arrow1(Scene):
	def construct(self):
		step1 = Text("Step 1")
		step2 = Text("Step 2")
		arrow = Arrow(LEFT,RIGHT)
		step1.move_to(LEFT*2)
		arrow.next_to(step1,RIGHT,buff = .1)
		step2.next_to(arrow,RIGHT,buff = .1)
		self.play(Write(step1))
		self.wait()
		self.play(GrowArrow(arrow))
		self.play(Write(step2))
		self.wait()
