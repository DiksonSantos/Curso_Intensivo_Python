import matplotlib.pyplot as plt
from Pagina_471_Classe_RandomWalk import Random_Walk

# Continua criando novos passeios enquanto o programa estiver ativo
while True:
    # Cria um passeio aleatório e plota os pontos
    rw = Random_Walk() #Chama a classe criando o Objeto 'rw'
    rw.fill_walk() #Chama o metodo  Para 'Andar' até atingir o 5Mil Pontos.
    plt.scatter(rw.x_values, rw.y_values, s=15) #Plotar Valores de X & Y
    plt.show()

    keep_running = input("Make another walk? (y/n): ")

    if keep_running == 'n':
        break

"""Cada vez que voce digita Y ele Plota um novo Grafico
de Bolinhas."""
