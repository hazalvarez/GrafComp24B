from manim import *
class MoveFrameBoxCopy2(Scene):
    def construct(self):
        text=MathTex(
            "\\frac{d}{dx}f(x)g(x)=","f(x)\\frac{d}{dx}g(x)","+",
            "g(x)\\frac{d}{dx}f(x)"
        )
        self.play(Write(text))
        framebox1 = SurroundingRectangle(text[1], buff = .1)
        framebox2 = SurroundingRectangle(text[3], buff = .1)
        t1 = MathTex("g'f")
        t2 = MathTex("f'g")
        t1.next_to(framebox1, UP, buff=0.1)
        t2.next_to(framebox2, UP, buff=0.1)
        self.play(
        	Create(framebox1),
        	FadeIn(t1)
        	)
        self.wait()
        self.play(
        	ReplacementTransform(framebox1.copy(),framebox2),
        	ReplacementTransform(t1.copy(),t2),
        	)
        self.wait()
