import csv

nome_arquivo = 'sitka_weather_2014.csv'
with open(nome_arquivo) as Objeto_CSV: #Transformamos num Objeto (qualquer).
    leitor = csv.reader(Objeto_CSV) #csv leitor -> Sabemos que o arquivo é um CSV então Usamos o Leitor Especifico.
    leitor_cru = next(leitor) #-> Isso serve p/ mostrar só o Cabeçalho do Arquivo CSV.
    print(leitor_cru) #Exibiu o Cabeçalho.

# O ENUMERATE PRECISA DE 2 ARGUMENTOS, UM P/ ATRIBUIR O NUMERO DA LINHA, O OUTRO P/ O CONTEUDO DA LISTA.
    for indice, coluna_header in enumerate(leitor_cru):
        #A FUNÇÃO ENUMERATE ENUMEROU CADA LINHA.
        print(indice, coluna_header) #FEZ O MESMO QUE NO PRIMEIRO PRINT, POREM COLOCOU LINHA A LINHA.

