from manim import *

class Plot2(Scene):
    def construct(self):
        self.camera.background_color = PURPLE
        # Crear los ejes
        axes = Axes(
            x_range=[0, 7, 1],  # [mínimo, máximo, frecuencia de ticks]
            y_range=[0, 50, 5],
            x_length=7,
            y_length=5,
            axis_config={"color": BLUE},
            tips=False,
        ).add_coordinates()

        # Crear el gráfico de la función
        graph = axes.plot(
            lambda x: x**2,
            color=GREEN,
        )
        # Animaciones
        self.play(Create(axes))         # Crear los ejes
        self.play(Create(graph), run_time=2)  # Crear el gráfico
        self.wait()
