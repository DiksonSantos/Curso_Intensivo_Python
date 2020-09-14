#Nome do arquivo na Apostila -> die.py

from random import randint

class Die():
    """Representa um DADO"""

    def __init__(self, num_lados=6):
        """Dado de Seis Lados"""
        self.Numero_Lados = num_lados

    def rola_dado(self):
        """Devolve um valor aleatório entre 1
         e o número de lados."""
        return randint(1, self.Numero_Lados)


#Pagina 483 -> Esta pedindo para criar outro arquivo.py e chamar a Classe a cima
#..mas não vou fazer isto.
#Nome do arquivo na Apostila -> die_visual.py

Dado = Die()

#Faz alguns lançamentos e armazena os resultados em uma lista

results = []
for rola_num in range(1000):
    result = Dado.rola_dado()
    results.append(result)
#print(results)

#Analisa os Resultados:
frequencies = []
for value in range(1, Dado.Numero_Lados+1):
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)

#Pagina 485 Criando Histograma:
#if __name__ == '__main__':
import pygal
# Visualiza os resultados
hist = pygal.Bar()
hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

#Legenda das Barras:
hist.add('D6 Lados', frequencies)

#Salvou o arquivo com esse nome ai:
hist.render_to_file('Dado_Visual.svg')
