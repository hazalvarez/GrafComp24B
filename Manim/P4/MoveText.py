from manim import *
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