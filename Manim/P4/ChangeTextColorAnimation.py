from manim import *

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
