import pygal

from Pagina_482_Pygal import Die

#Dois Dados:
Dado1 = Die()
Dado2 = Die()

#Alguns Lançamentos e Armazena Resultados em Uma Lista:
results = []

for rola_numero in range(1000):
    resul = Dado1.rola_dado() + Dado2.rola_dado()
    results.append(resul)

    #Analisa Resultados
    freuq = []
    max_resul = Dado1.Numero_Lados + Dado2.Numero_Lados
    for value in range(2, max_resul+1):
        freuquencia = results.count(value)
        freuq.append(freuquencia)

    #Visualiza Resultados
    hist = pygal.Bar()

    hist.title = "Results of rolling two D6 dice 1000 times."
    #Numeros que vão no Eixo X ou Horizontal da figura -> De 2 a 12 Jogadas de dados.
    hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    hist.x_title = "Result"
    hist.y_title = "Frequency of Result"
    #Legenda ao lado do Exito Y:
    hist.add('D6 + D6', freuq)
    #Salva para o Arquivo:
    hist.render_to_file('Pag_487_Pygal.svg')
