import csv
from datetime import datetime

from matplotlib import pyplot as plt

#Obter Datas e Temperaturas Maximas no Arquivo CSV:
#nome_arquivo = 'sitka_weather_07-2014.csv' #9 registros -> Na apostila Mostr 14
nome_arquivo = 'sitka_weather_2014.csv' #7 Registros -> Na ap = 12

with open(nome_arquivo) as Objeti_CSV:
    leitor = csv.reader(Objeti_CSV) #Metodo CSV.Leitor para ler estes tipos de arquivo.
    leitor_tosco = next(leitor) #Mostra Cabeçalho

    datas, high_temps = [], []
    for cru in leitor: #Cru São as Colunas (Eu Acho)
        #Percorreu a primeira coluna[0] e converteu as infs para Datas:
        data_atual = datetime.strptime(cru[0], "%Y-%m-%d")#Coluna 0 vai receber a Data\Hora
        datas.append(data_atual)#Jogou os dados convertidos na primeira lista Empacotada.

        alta = int(cru[1]) #Converteu a segunda COluna para INT
        high_temps.append(alta) #Segunda lista recebe Segunda Coluna INT. Ref as temperaturas.


#Plotagem dos Dados (Gráficos):
figura = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(datas, high_temps, c='purple')

# Formata o gráfico
plt.title("Daily high temperatures, 2014", fontsize=24)
plt.xlabel('RodaPé', fontsize=16)
#desenha os rótulos com as datas na diagonal para evitar que se sobreponham (falta espaço p/ expor todos).
figura.autofmt_xdate(rotation=40) #Descobri o Argumento Rotation Na internet -> Inclinação das descrições do Eixo X
plt.ylabel("Temperatura em (F)", fontsize=16)

#Documentação Sobre a Linha de Baixo  -> https://matplotlib.org/api/_as_gen/matplotlib.pyplot.tick_params.html
plt.tick_params(axis='x', which='minor', labelsize=16)
plt.show()


