from manim import *

class Plot5(Scene):
    def construct(self):
        self.camera.background_color = RED
        # Crear los ejes
        axes = Axes(
            x_range=[0, 7, 0.5],  # [mínimo, máximo, frecuencia de ticks]
            y_range=[0, 50, 10],  # [mínimo, máximo, frecuencia de ticks]
            x_length=7,
            y_length=5,
            axis_config={"color": BLUE},
            tips=False,
        )

        # Etiquetas personalizadas para el eje X
        custom_x_labels = {
            3.5: MathTex("3.5"),          # Etiqueta "3.5"
            4.5: MathTex(r"\frac{9}{2}"), # Etiqueta "9/2"
        }

        # Agregar etiquetas personalizadas al eje X
        for x_val, label in custom_x_labels.items():
            label.scale(0.7)
            label.next_to(axes.c2p(x_val, 0), DOWN)  # Posicionar la etiqueta
            self.add(label)

        # Crear el gráfico de la función
        graph = axes.plot(
            lambda x: x**2,
            x_range=[0, 7],
            color=GREEN,
        )

        # Animaciones
        self.play(Create(axes))  # Crear los ejes
        self.play(Create(graph), run_time=2)  # Crear el gráf
