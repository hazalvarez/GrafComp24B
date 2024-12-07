from manim import *
class TransformationText1V1(Scene):
	def construct(self):
		texto1 = Text("First text")
		texto2 = Text("Second text")
		self.play(Write(texto1))
		self.wait()
		self.play(Transform(texto1,texto2))
		self.wait()
