import matplotlib.pyplot as plt
from Pagina_471_Classe_RandomWalk import Random_Walk

# Continua criando novos passeios enquanto o programa estiver ativo
while True:
    # Cria um passeio aleatório e plota os pontos
    rw = Random_Walk() #Chama a classe criando o Objeto 'rw'
    rw.fill_walk() #Chama o metodo  Para 'Andar' até atingir o 5Mil Pontos.
    #plt.scatter(rw.x_values, rw.y_values, s=15) #Plotar Valores de X & Y
    point_numbers = list(range(rw.Num_Points))
    #Toda a magica esta nestas duas linhas a seguir: 'c'= Escala de Iluminancia.
    #Quanto mais alto o valor do numero, mais Claro é o pontinho.
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers,
                #colormap=mpl.colormap.Azul ->Cor do Pontinho Azul, Bordas do pontinho sem cor, Tamanho_Do_Pontinho=25
                cmap=plt.cm.Blues, edgecolor='none', s=25)

    # Enfatiza o primeiro e o último ponto (TRECHO NOVO PG 477):
    plt.scatter(0, 0, c='green', edgecolors='none', s=200)
    plt.scatter(rw.x_values[-1], rw.x_values[-1], c='red',
                edgecolors='none', s=100)

    # Remove os eixos  - (PAGINA 478):
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")

    if keep_running == 'n':
        break
