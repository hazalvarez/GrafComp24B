from manim import *
class MoveBracesCopy(Scene):
    def construct(self):
        text=MathTex(
            "\\frac{d}{dx}f(x)g(x)=","f(x)\\frac{d}{dx}g(x)","+",
            "g(x)\\frac{d}{dx}f(x)"
        )
        self.play(Write(text))
        brace1 = Brace(text[1], UP, buff = SMALL_BUFF)
        brace2 = Brace(text[3], UP, buff = SMALL_BUFF)
        t1 = brace1.get_text("$g'f$")
        t2 = brace2.get_text("$f'g$")
        self.play(
            GrowFromCenter(brace1),
            FadeIn(t1),
            )
        self.wait()
        self.play(
        	ReplacementTransform(brace1.copy(),brace2),
        	ReplacementTransform(t1.copy(),t2)
        	)
        self.wait()
