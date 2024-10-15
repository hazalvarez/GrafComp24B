#UNIVERSIDAD AUTONOMA DEL ESTADO DE MEXICO
#GRAFICACION COMPUTACIONAL
#RAUL ALEJANDRO CALDERON HERNANDEZ
#14 DE OCTUBRE DEL 2024 
#viendo como funciona la animacion de manim
from manim import *  # Asegúrate de usar la importación adecuada para la versión de Manim
import numpy as np

class OpeningManimExample(Scene):
    def construct(self):
        # Crear dos partes de texto
        text_part = Text("This is some ")  # Usar Text en lugar de TextMobject
        latex_part = Text("LaTeX")

        # Agrupar el texto normal y LaTeX en un VGroup
        title = VGroup(text_part, latex_part).arrange(RIGHT)
        
        # Fórmula de la serie de Basel usando MathTex
        basel = MathTex(
            r"\sum_{n=1}^\infty "
            r"\frac{1}{n^2} = \frac{\pi^2}{6}"
        )

        # Organizar los elementos verticalmente
        VGroup(title, basel).arrange(DOWN)

        # Animaciones
        self.play(Write(title))  # Escribe el título
        self.play(FadeIn(basel, shift=UP))  # Aparece la fórmula desde arriba
        self.wait()

        # Transformación del título
        transform_title = Text("That was a transform")
        transform_title.to_corner(UP + LEFT)

        self.play(Transform(title, transform_title))  # Transforma el título
        self.play(FadeOut(basel, shift=DOWN))  # Desvanece el basel hacia abajo
        self.wait()

        # Añadir el plano de números (grid)
        grid = NumberPlane()
        grid_title = Text("This is a grid")
        grid_title.scale(1.5)
        grid_title.move_to(transform_title)

        self.add(grid, grid_title)  # Asegura que el título esté sobre el grid
        self.play(FadeOut(title), FadeIn(grid_title, shift=DOWN), Write(grid))  # Animaciones del grid
        self.wait()

        # Transformación no lineal aplicada al grid
        grid_transform_title = Text(
            "That was a non-linear function \\\\"
            "applied to the grid"
        )
        grid_transform_title.move_to(grid_title, UP + LEFT)

        # Preparar la transformación no lineal
        non_linear_transformation = grid.animate.apply_function(
            lambda p: p + np.array([
                np.sin(p[1]),
                np.sin(p[0]),
                0,
            ])
        )

        # Aplicar transformación no lineal al grid
        self.play(non_linear_transformation, run_time=3)  # Usa el objeto animado
        self.wait()

        # Transformación del título del grid
        self.play(Transform(grid_title, grid_transform_title))
        self.wait()
