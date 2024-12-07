from manim import *

class TransformationText2(Scene):
	def construct(self):
		text1 = Text("Function")
		text2 = Text("Derivative")
		text3 = Text("Integral")
		text4 = Text("Transformation")
		self.play(Write(text1))
		self.wait()
		#Trans text1 -> text2
		self.play(ReplacementTransform(text1,text2))
		self.wait()
		#Trans text2 -> text3
		self.play(ReplacementTransform(text2,text3))
		self.wait()
		#Trans text3 -> text4
		self.play(ReplacementTransform(text3,text4))
		self.wait()
