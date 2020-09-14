from random import choice

class Random_Walk():
    """Gera passeios aleatorios"""

    def __init__(self, num_points=500):
        self.Num_Points = num_points

        #Todos os passeios começam em (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calcula todos os Pontos do Passeio"""
        #Continua dando passos até que o passeio alcance o tamanho desejado.
#Quanto mais anda Mais marca pontos, enquanto x_val Menor que Numero_De_Pontos, COntinua Andando.
        while len(self.x_values) < self.Num_Points:

            #Decide direção a ser seguida & distancia a ser percorrida nessa direção.
            x_direction = choice([1, -1])
            #qual é a distância a ser percorrida nessa direção
            x_distance = choice([0, 1, 2, 3, 4])
            x_steps = x_direction * x_distance
            #Movimentos P Esq E Dir
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Rejeito Movimentos que não vão a lugar Nenhum.
            if x_steps == 0 and y_step == 0:
                continue

            # Calcula os próximos valores de x e de y
            next_x = self.x_values[-1] + x_steps
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
"""
import matplotlib.pyplot as plt

# Cria um passeio aleatório e plota os pontos
rw = Random_Walk()
#Os passos do passeio foram armazenados aqui:
rw.fill_walk() #Aqui é um metodo sendo chamado.
#Para plotar como Pontinhos na tela, a trajetoria.
plt.scatter(rw.x_values, rw.y_values, s=15)# s=Tamanho dos Pontinhos.
#Mostra Gráfico com 5.000 pontos na tela.
plt.show()
"""
