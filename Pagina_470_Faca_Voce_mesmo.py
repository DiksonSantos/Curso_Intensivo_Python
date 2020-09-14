import matplotlib.pyplot as plt
"""
#15.1 - Cubos:
import matplotlib.pyplot as plt

x_valores = list(range(0, 6))
y_valores = [x**3 for x in x_valores]

plt.title("Cubos", fontsize=21)
plt.ylabel("Eixo Y", fontsize=10)
plt.xlabel("Eico X", fontsize=10)
plt.tick_params(axis='both', labelsize=15)

plt.scatter(x_valores, y_valores, edgecolors='none', s=45)
#plt.pie(x_valores)
plt.show()
#print(y_valores)
"""

# 15.2 Cubos Coloridos:

x_valores = list(range(5001))
y_valores = [x**3 for x in x_valores]
                                                      #s=Espessura da Risca.
plt.scatter(x_valores, y_valores , edgecolors='purple', s=0.01)
plt.title("Cubos", fontsize=28)
plt.xlabel('Valores', fontsize=14)
plt.ylabel('Valores dos Cubos', fontsize=14)
plt.tick_params(axis='both', labelsize=17)
#Não entendi o que esta linha faz ??? A Não ser -> Onde a linha começa.
#plt.axis([0, 5100, 0, 5100**3])

plt.show()
