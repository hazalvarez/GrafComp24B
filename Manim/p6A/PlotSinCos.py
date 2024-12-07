from manim import *

class PlotSinCos(Scene):
    def construct(self):
        self.camera.background_color = DARK_BLUE
        # Crear los ejes
        axes = Axes(
            x_range=[-3 * PI / 2, 3 * PI / 2, PI / 2],  # [mínimo, máximo, frecuencia de ticks]
            y_range=[-1.5, 1.5, 0.5],  # [mínimo, máximo, frecuencia de ticks]
            x_length=6,
            y_length=3,
            axis_config={"color": BLUE},
            tips=False,
        )

        # Crear los gráficos de seno y coseno
        plot_sin = axes.plot(
            lambda x: np.sin(x),  # Función seno
            color=GREEN,
            x_range=[-3 * PI / 2, 3 * PI / 2],
        )
        plot_cos = axes.plot(
            lambda x: np.cos(x),  # Función coseno
            color=GRAY,
            x_range=[-3 * PI / 2, 3 * PI / 2],
        )

        # Establecer grosor de las líneas
        plot_sin.set_stroke(width=3)
        plot_cos.set_stroke(width=2)

        # Etiquetas de funciones
        sin_label = axes.get_graph_label(plot_sin, label='\\sin(x)')
        cos_label = axes.get_graph_label(plot_cos, label='\\cos(x)')

        # Animaciones
        self.play(Create(axes))  # Crear los ejes
        self.play(Create(plot_sin), Create(plot_cos), run_time=2)  # Crear los gráficos
        self.play(Write(sin_label), Write(cos_label))  # Escribir las leyendas
        self.wait()

        # Añadir etiquetas de los ejes X y Y
        func = MathTex("\\sin\\theta")
        var = MathTex("\\theta")
        func.set_color(BLUE)
        var.set_color(PURPLE)
        func.next_to(axes.y_axis, UP)
        var.next_to(axes.x_axis, RIGHT + UP)
        
        # Etiquetas personalizadas para los valores en el eje X
        values_x = [
            (-3 * PI / 2, "-\\frac{3\\pi}{2}"),
            (-PI, "-\\pi"),
            (-PI / 2, "-\\frac{\\pi}{2}"),
            (0, "0"),
            (PI / 2, "\\frac{\\pi}{2}"),
            (PI, "\\pi"),
            (3 * PI / 2, "\\frac{3\\pi}{2}"),
        ]

        # Crear las etiquetas personalizadas para el eje X
        x_axis_labels = VGroup()
        for x_val, label in values_x:
            label_tex = MathTex(label)
            label_tex.scale(0.7)
            label_tex.next_to(axes.c2p(x_val, 0), DOWN)
            x_axis_labels.add(label_tex)

        # Animaciones para las etiquetas de los ejes
        self.play(
            Write(axes.x_axis),
            Write(axes.y_axis),
            Write(x_axis_labels),
            Write(func),
            Write(var),
            run_time=2
        )
