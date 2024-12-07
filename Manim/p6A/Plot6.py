from manim import *

class Plot6(Scene):
    def construct(self):
        self.camera.background_color = MAROON
        # Crear los ejes
        axes = Axes(
            x_range=[0, 7, 0.5],  # [mínimo, máximo, frecuencia de ticks]
            y_range=[0, 50, 10],  # [mínimo, máximo, frecuencia de ticks]
            x_length=7,
            y_length=5,
            axis_config={"color": BLUE},
            tips=False,
        )

        # Lista de valores decimales para el eje X
        values_decimal_x = [0, 0.5, 1, 1.5, 3.35]

        # Crear etiquetas para los valores en el eje X
        for x_val in values_decimal_x:
            tex_label = MathTex(f"{x_val}")  # Convertir a LaTeX
            tex_label.scale(0.7)  # Escalar la etiqueta
            tex_label.next_to(axes.c2p(x_val, 0), DOWN)  # Posicionar debajo del eje
            self.add(tex_label)  # Añadir etiqueta a la escena

        # Crear el gráfico de la función
        graph = axes.plot(
            lambda x: x**2,
            x_range=[0, 7],
            color=GREEN,
        )

        # Animaciones
        self.play(Create(axes))  # Crear los ejes
        self.play(Create(graph), run_time=2)  # Crear el gráfico
        self.wait()
