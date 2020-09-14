import json

#Carrega os Dados Numa Lista:
nome_arquivo = 'population_data.json'
with open(nome_arquivo) as Objeto:
    pop_data = json.load(Objeto) #Load Converte o JSON para uma Lista.

#Exibe a População de Cada País em 2010:
for pop_dic in pop_data: #pop_data possuio o Objeto JSON
#Nesta Linha a baixo tudo é determinado, Ou seja, se o que estiver na coluna 'Year' for == ao especificado, as Variaveis
#..nas linhas a baixo receberão informações deste Couchete do arquivo JSON.
    #if pop_dic['Year'] == '2010':  #ORIGINAL
     if pop_dic['Country Name'] == 'Brazil' and pop_dic['Year'] == '2010': #CUSTOMIZEI.
        nome_pais = pop_dic['Country Name']
        population = pop_dic['Value']
        codigo_pais = pop_dic['Country Code'] #Eu coloquei esta Variavel aqui.
        print(nome_pais + ": "+population, " - ", codigo_pais)

