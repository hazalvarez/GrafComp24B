#UNIVERSIDAD AUTONOMA DEL ESTADO DE MEXICO
#GRAFICACION COMPUTACIONAL
#RAUL ALEJANDRO CALDERON HERNANDEZ
#14 DE OCTUBRE DEL 2024 

from manim import *
import numpy as np
class Shapes(Scene):
  def construct(self):
    circulo = Circle() # Creación de circulo
    createCircle = Create(circulo) # Animación de creación
    self.play(createCircle) # Mostrar la animación
    fadeOutCircle = FadeOut(circulo) # Animación de desaparición
    self.play(fadeOutCircle) # Mostrar la animación
    rect = Rectangle(color="blue", height=3, width=1)
    self.play(Create(rect))
    self.play(FadeOut(rect))
    cuadrado = Square(color="blue") # Cuadrado
    cuadrado2 = Square(color="pink")
    cuadrado4 = Square(color="purple")
    cuadrado3 = Square(color="orange")
    
    cuadrado.move_to(np.array([-4, 2, 0])) # Llevas al cuadrado a la coordenada
    cuadrado2.to_edge(np.array([4, -2, 4])) # LLeva una figura al borde
    cuadrado4.to_edge(np.array([4, 2, 4])) # LLeva una figura al borde
    cuadrado3.to_edge(np.array([-4, -2, 0])) # LLeva una figura al borde
    
    # Hay cuatro direcciónes UP, LEFT, RIGHT, DOWN
    self.play(Create(cuadrado), Create(cuadrado2),Create(cuadrado3), Create(cuadrado4))
    self.play(FadeOut(cuadrado), FadeOut(cuadrado2),FadeOut(cuadrado4), FadeOut(cuadrado3))
