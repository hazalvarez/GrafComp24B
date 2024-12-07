from manim import *
class CopyTwoFormulas2(Scene):
	def construct(self):
		formula1 = MathTex(
				"\\neg","\\forall","x",":","P(x)"
			)
		formula2 = MathTex(
				"\\exists","x",":","\\neg","P(x)"
			)
		for tam,pos,formula in [(2,2*UP,formula1),(2,2*DOWN,formula2)]:
			formula.scale(tam)
			formula.move_to(pos)
		self.play(Write(formula1))
		self.wait()
		changes = [
			# First time
			[(2,3,4),
			# | | |
			# v v v
			 (1,2,4)],
			# Second time
			[(0,),
			# | 
			# v
			 (3,)],
			# Third time
			[(1,),
			# | 
			# v
			 (0,)]
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
