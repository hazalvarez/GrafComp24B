from manim import *

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

