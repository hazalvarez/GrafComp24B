from manim import *

class Plot1(Scene):
    def construct(self):
        self.camera.background_color = DARK_GRAY
        axes = Axes(
            x_range=[0, 7, 0.5],  # [mínimo, máximo, frecuencia de ticks]
            y_range=[0, 50, 5],
            x_length=7,
            y_length=5,
            axis_config={"color": BLUE},
            tips=False,
        )
        # Crear el gráfico de la función
        graph = axes.plot(
            lambda x: x**2,
            x_range=[2, 4],  # Rango del gráfico
            color=GREEN,
        )

        # Etiquetar el gráfico
        graph_label = axes.get_graph_label(
            graph, label="x^2", x_val=3.5, direction=UP
        )

        # Animaciones
        self.play(Create(axes))         # Animar la creación de los ejes
        self.play(Create(graph))        # Animar la creación del gráfico
        self.play(Write(graph_label))   # Animar la etiqueta del gráfico
        self.wait()  # Pausa al final para ver el resultado
