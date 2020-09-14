import json
from Pag_514_Country_Codes import pega_cod_pais

Pais = str(input("Pais: ")).strip()
#Carrega os Dados Numa Lista:
nome_arquivo = 'population_data.json'
with open(nome_arquivo) as Objeto:
    pop_data = json.load(Objeto) #Load Converte o JSON para uma Lista.

#Exibe a População de Cada País em 2010:
for pop_dic in pop_data: #pop_data possuio o Objeto JSON
#Nesta Linha a baixo tudo é determinado, Ou seja, se o que estiver na coluna 'Year' for == ao especificado, as Variaveis
#..nas linhas a baixo receberão informações deste Couchete do arquivo JSON.
    if pop_dic['Year'] == '2010':
        nome_pais = pop_dic['Country Name']
        #No Livro pediu INT mas NÃO funcionou. Usei FLOAT, e funcionou perfeitamente. Já o INT antes do FLOAT foi ideia do Livro.
        #..sempre a função que esta no interior dos() é executada Primeiro (neste caso a FLOAT).
        population = int(float(pop_dic['Value'])) #AQUI FOI FEITA A CONVERSÃO PARA NUMERICO.
        codigo = pega_cod_pais(Pais)
        if codigo:
            print(codigo + ": " + str(population))
        else:
            print("Erro - " + Pais)


