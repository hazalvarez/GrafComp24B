from manim import *

class Plot7(Scene):
    def construct(self):
        # Crear los ejes
        self.camera.background_color = GOLD
        axes = Axes(
            x_range=[0, 7, 0.5],  # [mínimo, máximo, frecuencia de ticks]
            y_range=[0, 50, 10],  # [mínimo, máximo, frecuencia de ticks]
            x_length=7,
            y_length=5,
            axis_config={"color": BLUE},
            tips=False,
        )

        # Generar valores decimales en el eje X
        values_decimal_x = np.arange(0, 7.5, 0.5)

        # Crear etiquetas para los valores en el eje X
        for x_val in values_decimal_x:
            tex_label = MathTex(f"{x_val:.1f}")  # Etiqueta en formato decimal
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
