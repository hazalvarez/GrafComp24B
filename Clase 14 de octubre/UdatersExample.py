#UNIVERSIDAD AUTONOMA DEL ESTADO DE MEXICO
#GRAFICACION COMPUTACIONAL
#RAUL ALEJANDRO CALDERON HERNANDEZ
#14 DE OCTUBRE DEL 2024 

from manim import *  # Importar la biblioteca de Manim
import numpy as np

class UdatersExample(Scene):
    def construct(self):
        # Crear un número decimal inicial
        decimal = DecimalNumber(
            0,
            show_ellipsis=True,
            num_decimal_places=3,
            include_sign=True,
        )
        # Crear un cuadrado y colocarlo en la parte superior
        square = Square().to_edge(UP)

        # Agregar un actualizador para el decimal
        decimal.add_updater(lambda d: d.next_to(square, RIGHT))
        
        # Agregar un actualizador que se encarga de cambiar el valor del decimal
        decimal.add_updater(lambda d: d.set_value(square.get_center()[1]))

        # Agregar el cuadrado y el decimal a la escena
        self.add(square, decimal)

        # Animar el cuadrado moviéndose hacia abajo y de regreso
        self.play(
            square.animate.to_edge(DOWN),  # Cambiado a animate
            rate_func=there_and_back,
            run_time=5,
        )
        
        self.wait()  # Esperar al final
