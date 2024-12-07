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

class Plot3(Scene):
    def construct(self):
        self.camera.background_color = ORANGE
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
