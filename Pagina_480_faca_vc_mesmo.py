
"""
Decidi só copiar das respostas e analisar. Já fiz algumas alterações parecidas nos
codigos durante a leitura do Livro.

"""

#15.5    -> Os anteriores eu já fiz alterações similares
import matplotlib.pyplot as plt
from Pagina_471_Classe_RandomWalk import Random_Walk

from random import choice


class RandomWalk():
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """Determine the direction and distance for a step."""
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance
        return step

    def fill_walk(self):
        """Calculate all the points in the walk."""

        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:


            # Enquanto o valor de 'x_values' for menor que 5000 (que é a var numpoints).
            #..continue multiplicando as Duas listas de 'get_step' , e guardando-os nestas
            #..duas var locais aqui:
            x_step = self.get_step()
            y_step = self.get_step()

            # Reject moves that go nowhere. -Se por um acaso os resultados chegarem a ZEROs ->Continue.
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the next x and y values.
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

#Aqui as primeiras variaveis da primeira fun, absorvem os resultados dos calculos de
            #..criação dos proximos passos:
            self.x_values.append(next_x)
            self.y_values.append(next_y)


            plt.show()




"""
NADA FUNCIONA AQUI. TENTEI IMPORTAR ESTE MODULO EM OTROS SCRIPSTS COMO FOI FEITO
NOS EXERCICIOS ANTERIORES, MAS DA PAU, E SOZINHO, NADA FUNCIONA AQUI.


NÃO ADIANTA. DEVO TER COMIDO BRONHA ESTA DESGRAÇA DE CODIGO NÃO FAZ PORRA NENHUMA!

DEIXAREI ESSE SATANAZ DE LADO E SEGUIREI COM O LIVRO
"""
