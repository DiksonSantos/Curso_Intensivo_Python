import matplotlib.pyplot as plt

"""
#Não tem explicação Nenhuma na apostila, não fez sentido

#plt.scatter(4, 8)
#plt.show()

plt.scatter(2, 4, s=200)

#Cabeçalho:
plt.title("Titulo: Numeros ao Quadrado", fontsize=20)

#Rodapé:
plt.xlabel("Valores", fontsize=14)

#Eixo Vertica (Y):
plt.ylabel("Square of Value", fontsize=14)

plt.show()
"""
"""Mostrou Pntos Azuis no Gráfico de acordo com a posição dos numeros da listas a baixo:"""
#x_valores = [1,2,3,4,5]
#y_valores = [1,4,9,16,25]

x_valores = list(range(1,999))
y_valores = [x**2 for x in x_valores]

# ???? Mudou NADA:
plt.scatter(x_valores, y_valores, s=40)


#plt.ylabel("Quadrado dos Valores", fontsize=1)
plt.title("Numeros Quadrados", fontsize=25)
plt.xlabel("Valores", fontsize=16) #Até 20 da pra visualizar.
plt.ylabel('Quadrados', fontsize=12)# Até tam 12 OK

#Tamanho da fonte dos Numeros de X e Y
plt.tick_params(axis='both', labelsize=8)

#ATENÇÃO -> SE NÃO MENSIONAR AS DUAS LINHAS = NÃO FUNCIONA
plt.plot(y_valores, linewidth=1)
plt.plot(x_valores, linewidth=1)


#Intervalos para serem mostrados em cada eixo:
plt.axis([0, 1100, 0, 1100000])


#Variação de cor da Linha Azul:
plt.scatter(x_valores, y_valores, edgecolor='purple', s=14)

#Blue -> Linha dentro da linha red. Red -> Contorno da linha Blue, e Ponta dela tbm.
plt.scatter(x_valores, y_valores, c='blue', edgecolor='red', s=5)
plt.show()



