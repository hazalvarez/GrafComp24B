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

class CopyTextV2(Scene):
	def construct(self):
		formula = MathTex("\\frac{d}{dx}",
			"(","u","+","v",")","=",
			"\\frac{d}{dx}","u","+","\\frac{d}{dx}","v"
			)
		formula.scale(2)
		self.play(Write(formula[0:7]))
		self.wait()
		self.play(
			ReplacementTransform(formula[2].copy(),formula[8]),
			ReplacementTransform(formula[4].copy(),formula[11]),
			ReplacementTransform(formula[3].copy(),formula[9]),
			run_time=3
			)
		self.wait()
		self.play(
			ReplacementTransform(formula[0].copy(),formula[7]),
			ReplacementTransform(formula[0].copy(),formula[10]),
			run_time=3
			)
		self.wait()

class CopyTextV3(Scene):
	def construct(self):
		formula = MathTex("\\frac{d}{dx}",
			"(","u","+","v",")","=",
			"\\frac{d}{dx}","u","+","\\frac{d}{dx}","v"
			)
		formula.scale(2)
		formula[8].set_color(RED)
		formula[11].set_color(BLUE)
		self.play(Write(formula[0:7]))
		self.wait()
		self.play(
			ReplacementTransform(formula[2].copy(),formula[8]),
			ReplacementTransform(formula[4].copy(),formula[11]),
			ReplacementTransform(formula[3].copy(),formula[9]),
			run_time=3
			)
		self.wait()
		self.play(
			ReplacementTransform(formula[0].copy(),formula[7]),
			ReplacementTransform(formula[0].copy(),formula[10]),
			run_time=3
			)
		self.wait()

class CopyTextV4(Scene):
	def construct(self):
		formula = MathTex("\\frac{d}{dx}",
			"(","u","+","v",")","=",
			"\\frac{d}{dx}","u","+","\\frac{d}{dx}","v"
			)
		formula.scale(2)
		for letter,color in [("u",RED),("v",BLUE)]:
			formula.set_color_by_tex(letter,color)
		self.play(Write(formula[0:7]))
		self.wait()
		self.play(
			ReplacementTransform(formula[2].copy(),formula[8]),
			ReplacementTransform(formula[4].copy(),formula[11]),
			ReplacementTransform(formula[3].copy(),formula[9]),
			run_time=3
			)
		self.wait()
		self.play(
			ReplacementTransform(formula[0].copy(),formula[7]),
			ReplacementTransform(formula[0].copy(),formula[10]),
			run_time=3
			)
		self.wait()

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

class CopyTwoFormulas3(Scene):
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
					formula1[i],formula2[j]
					)
				for i,j in zip(pre_ind,post_ind)
				],
				run_time=2
			)
			self.wait()


class ChangeTextColorAnimation(Scene):
    def construct(self):
        # Crear el texto y escalarlo
        text = Text("Text", font_size=144)  # Fuente ajustada directamente
        self.play(Write(text))
        self.wait()

        # Cambiar el color del texto a amarillo con una animación
        self.play(text.animate.set_color(YELLOW), run_time=2)
        self.wait()

        # Cambiar el color gradualmente a un gradiente
        gradient_colors = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]
        self.play(text.animate.set_color_by_gradient(*gradient_colors), run_time=3)
        self.wait()

class ChangeSizeAnimation(Scene):
    def construct(self):
        text = Text("Text", font_size=72)  # Ajuste del tamaño inicial
        self.play(Write(text))
        self.wait()

        # Escalar el texto con animación
        self.play(text.animate.scale(3), run_time=2)
        self.wait()

        # Reducir el tamaño nuevamente para mostrar un ciclo
        self.play(text.animate.scale(0.5), run_time=2)
        self.wait()
class MoveText(Scene):
    def construct(self):
        text = Text("Text", font_size=72)
        text.shift(LEFT * 2)  # Posición inicial
        self.play(Write(text))
        self.wait()

        # Mover el texto hacia la derecha con un arco suave
        self.play(
            text.animate.shift(RIGHT * 4),  # Movimiento
            rate_func=there_and_back,  # Hace que el texto regrese a la posición inicial
            path_arc=-PI / 2,  # Arco hacia abajo
            run_time=4
        )
        self.wait()
class ChangeColorAndSizeAnimation(Scene):
    def construct(self):
        text = Text("Text", font_size=72)
        text.shift(LEFT * 2)  # Posición inicial
        self.play(Write(text))
        self.wait()

        # Animación combinada: cambiar tamaño, color y posición
        self.play(
            text.animate.shift(RIGHT * 4).scale(2).set_color(RED),
            run_time=3
        )
        self.wait()

        # Restaurar propiedades originales
        self.play(
            text.animate.shift(LEFT * 4).scale(0.5).set_color(WHITE),
            run_time=3
        )
        self.wait()

