#UNIVERSIDAD AUTONOMA DEL ESTADO DE MEXICO
#GRAFICACION COMPUTACIONAL
#RAUL ALEJANDRO CALDERON HERNANDEZ
#14 DE OCTUBRE DEL 2024 

from manim import *  # Asegúrate de usar la importación adecuada para la versión de Manim
import numpy as np

class WarpSquare(Scene):
    def construct(self):
        square = Square()
        self.play(ApplyPointwiseFunction(
            lambda point: complex_to_R3(np.exp(R3_to_complex(point))),
            square
        ))
        self.wait()
