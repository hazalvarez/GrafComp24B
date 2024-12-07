from manim import *
ColoresFondo = [BLUE,RED,BLACK,ORANGE,PURPLE,"#ff7f7f","#ff7f7f","#ff7f7f","#ff7f7f",GRAY,"#ff7f7f"
				,"#ff7f7f",GREEN,"#ff7f7f","#205400"]
class MoveBraces(Scene):
    def construct(self):
        text=MathTex(
            "\\frac{d}{dx}f(x)g(x)=",       #0
            "f(x)\\frac{d}{dx}g(x)",        #1
            "+",                            #2
            "g(x)\\frac{d}{dx}f(x)"         #3
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
        	ReplacementTransform(brace1,brace2),
        	ReplacementTransform(t1,t2)
        	)
        self.wait()
        
        