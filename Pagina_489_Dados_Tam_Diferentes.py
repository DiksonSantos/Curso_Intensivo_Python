from Pagina_482_Pygal import Die

import pygal
# Cria um D6 e um D10
Dado1 = Die()
Dado2 = Die(10)
# Faz alguns lançamentos e armazena os resultados em uma lista
results = []
for roll_num in range(50000):
    result = Dado1.rola_dado() + Dado2.rola_dado()
    results.append(result)

# Analisa os resultados
freuq = []
max_resul = Dado1.Numero_Lados + Dado2.Numero_Lados
for value in range(2, max_resul+1):
    freuquencia = results.count(value)
    freuq.append(freuquencia)

# Visualiza os resultados
hist = pygal.Bar()
hist.title = "Results of rolling a D6 and a D10 50,000 times."
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11','12','13', '14', '15', '16']
hist.x_title = "Result"
hist.y_title = "Frequency Result"

hist.add('D6 + D10', freuq)
hist.render_to_file('Dados_Diferentes_489.svg')

#CONTINUA NA 491
