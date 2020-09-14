import csv
from datetime import datetime

from matplotlib import pyplot as plt


nome_arquivo = 'sitka_weather_2014.csv' #7 Registros -> Na ap = 12

with open(nome_arquivo) as Objeti_CSV:
    leitor = csv.reader(Objeti_CSV) #Metodo CSV.Leitor para ler estes tipos de arquivo.
    leitor_tosco = next(leitor) #Mostra Cabeçalho

    datas, high_temps, lows = [], [], []
    for cru in leitor: #Cru São as Colunas (Eu Acho)
        #Percorreu a primeira coluna[0] e converteu as infs para Datas:
        data_atual = datetime.strptime(cru[0], "%Y-%m-%d")#Coluna 0 vai receber a Data\Hora
        datas.append(data_atual)#Jogou os dados convertidos na primeira lista Empacotada.

        alta = int(cru[1]) #Converteu a segunda COluna para INT
        high_temps.append(alta) #Segunda lista recebe Segunda Coluna INT. Ref as temperaturas.

        low = int(cru[3]) #Terceira Coluna Referente a Temperaturas mais BAIXAS
        lows.append(low)

#Listas ->  dates, highs, lows = [], [], []
#Plotagem dos Gráficos:
figura = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(datas, high_temps, c='red', alpha=0.5)
plt.plot(datas, lows, c='blue', alpha=0.5)
plt.fill_between(datas, high_temps, lows, facecolor='blue', alpha=0.2)
plt.plot(datas, high_temps, c='red')
plt.plot(datas, lows, c='blue') #Linha AZUL para as temperaturas Baixas.

# Formata o gráfico
plt.title("Daily High and LOW temperatures, 2014", fontsize=24)
plt.xlabel('', fontsize=16)
#desenha os rótulos com as datas na diagonal para evitar que se sobreponham (falta espaço p/ expor todos).
figura.autofmt_xdate()
plt.ylabel("Temperatura em (F)", fontsize=16)

plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()


#CONTINUA NA PAG 506
