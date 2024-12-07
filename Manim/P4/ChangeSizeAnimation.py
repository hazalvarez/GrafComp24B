from manim import *
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