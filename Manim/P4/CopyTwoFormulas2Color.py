from manim import *
class CopyTwoFormulas2Color(Scene):
	def construct(self):
		formula1 = MathTex(
				"\\neg","\\forall","x",":","P(x)"
			)
		formula2 = MathTex(
				"\\exists","x",":","\\neg","P(x)"
			)
		parametters = [(2,2*UP,formula1,GREEN,"\\forall"),
					  (2,2*DOWN,formula2,ORANGE,"\\exists")]
		for size,pos,formula,col,sim in parametters:
			formula.scale(size)
			formula.move_to(pos)
			formula.set_color_by_tex(sim,col)
			formula.set_color_by_tex("\\neg",PINK)
		self.play(Write(formula1))
		self.wait()
		changes = [
			[(2,3,4),(1,2,4)],
			[(0,),(3,)],
			[(1,),(0,)]
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
