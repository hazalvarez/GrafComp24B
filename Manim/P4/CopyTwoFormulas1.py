from manim import *
class CopyTwoFormulas1(Scene):
	def construct(self):
		formula1 = MathTex(
				"\\neg",		#0
				"\\forall",		#1
				"x",			#2
				":",			#3
				"P(x)"			#4
			)
		formula2 = MathTex(
				"\\exists",		#0
				"x",			#1
				":",			#2
				"\\neg",		#3
				"P(x)"			#4
			)
		for size,pos,formula in [(2,2*UP,formula1),(2,2*DOWN,formula2)]:
			formula.scale(size)
			formula.move_to(pos)
		self.play(Write(formula1))
		self.wait()
		changes = [
			[(0,1,2,3,4),
			# | | | | |
			# v v v v v
			 (3,0,1,2,4)],
		]
		for pre_ind,post_ind in changes:
			self.play(*[
				ReplacementTransform(
					formula1[i].copy(),formula2[j]
					)
				for i,j in zip(pre_ind,post_ind)
				],
				run_time=2
			)
			self.wait()
