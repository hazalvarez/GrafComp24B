from manim import *

class Plot4(Scene):
    def construct(self):
        self.camera.background_color = BLACK
        # Crear los ejes
        axes = Axes(
            x_range=[0, 7, 1],  # [mínimo, máximo, frecuencia de ticks]
            y_range=[0, 50, 5],
            x_length=7,
            y_length=5,
            axis_config={"color": BLUE},
            tips=False,
        )

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
