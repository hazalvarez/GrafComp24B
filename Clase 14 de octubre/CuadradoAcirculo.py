#UNIVERSIDAD AUTONOMA DEL ESTADO DE MEXICO
#GRAFICACION COMPUTACIONAL
#RAUL ALEJANDRO CALDERON HERNANDEZ
#14 DE OCTUBRE DEL 2024 
#CONVERTIR DE CIRCULO A CUADRADO
from manim import *
import numpy as np

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))
