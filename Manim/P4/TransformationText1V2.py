from manim import *
class TransformationText1V2(Scene):
	def construct(self):
		texto1 = Text("First text")
		texto1.to_edge(UP)
		texto2 = Text("Second text")
		self.play(Write(texto1))
		self.wait()
		self.play(Transform(texto1,texto2))
		self.wait()
