#UNIVERSIDAD AUTONOMA DEL ESTADO DE MEXICO
#GRAFICACION COMPUTACIONAL
#RAUL ALEJANDRO CALDERON HERNANDEZ
#14 DE OCTUBRE DEL 2024 

from manim import *

class WriteStuff(Scene):
    def construct(self):
        example_text = Text(
            "This is some text",  # Cambia TextMobject por Text
            t2c={"text": YELLOW}  # Colorea la palabra "text" de amarillo
        )
        example_tex = MathTex(
            "\\sum_{k=1}^\\infty {1 \\over k^2} = {\\pi^2 \\over 6}"
        )
        group = VGroup(example_text, example_tex)
        group.arrange(DOWN)  # Coloca los textos uno debajo del otro
        group.set_width(config.frame_width - 2 * LARGE_BUFF)

        # Animaciones
        self.play(Write(example_text))
        self.play(Write(example_tex))
        self.wait()
