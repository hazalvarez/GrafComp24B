from manim import *
class CopyTextV1(Scene):
	def construct(self):
		formula = MathTex(
			"\\frac{d}{dx}", #0
			"(", #1
			"u", #2
			"+", #3
			"v", #4
			")", #5
			"=", #6
			"\\frac{d}{dx}", #7
			"u", #8
			"+", #9
			"\\frac{d}{dx}", #10
			"v" #11
			)
		formula.scale(2)
		self.play(Write(formula[0:7]))
		self.wait()
		self.play(
			ReplacementTransform(formula[2].copy(),formula[8]),
			ReplacementTransform(formula[4].copy(),formula[11]),
			ReplacementTransform(formula[3].copy(),formula[9])
			)
		self.wait()
		self.play(
			ReplacementTransform(formula[0].copy(),formula[7]),
			ReplacementTransform(formula[0].copy(),formula[10])
			)
		self.wait()
