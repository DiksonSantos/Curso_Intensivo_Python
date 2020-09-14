import matplotlib.pyplot as plt

"""
Como gerar Varios tipos de Graficos neste site tem as funções
ou comandos:
https://matplotlib.org/tutorials/introductory/sample_plots.html

"""
Valores_De_Entrada = [1, 2, 3, 4, 5]
quadrados = [1, 4, 9, 16, 25]

plt.plot(Valores_De_Entrada, quadrados, linewidth=5)
#plt.plot(quadrados)
#plt.show()

#Altera Expessura da Linha do Gráfico.
plt.plot(quadrados, linewidth=3)
#plt.show()

#Colocou um Titulo/Cabeçalho no Grafico:
plt.title("Numeros Quadrados", fontsize=25)
#plt.show()

#O que vai escrito no RODAPÉ e seu tamanho:
plt.xlabel("Valores", fontsize=16) #Até 20 da pra visualizar.
#plt.show()

#Escrito na ascendente do lado Esquerdo do Gráfico:
plt.ylabel("Quadrado dos Valores", fontsize=18)
#plt.show()

#O Tamanho dos Numeros que aparecem nos Eixos X & Y do Graf
plt.tick_params(axis='both', labelsize=14)
plt.show()



