#death_valley_2014.csv

import csv
from datetime import datetime

from matplotlib import pyplot as plt


nome_arquivo = 'death_valley_2014.csv' #7 Registros -> Na ap = 12

with open(nome_arquivo) as Objeti_CSV:
    leitor = csv.reader(Objeti_CSV) #Metodo CSV.Leitor para ler estes tipos de arquivo.
    leitor_tosco = next(leitor) #Mostra Cabeçalho

    datas, high_temps, lows = [], [], []
    for cru in leitor: #Cru São as Colunas (Eu Acho)
        try:
            data_atual = datetime.strptime(cru[0], "%Y-%m-%d")
            alta = int(cru[1])
            low = int(cru[3])
        except ValueError:
            print(data_atual, "Data Faltante")
        else:
            datas.append(data_atual)
            high_temps.append(alta)
            lows.append(low)

figura = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(datas, high_temps, c='red', alpha=0.5)
plt.plot(datas, lows, c='blue', alpha=0.5)
plt.fill_between(datas, high_temps, lows, facecolor='blue', alpha=0.2)
plt.plot(datas, high_temps, c='red')
plt.plot(datas, lows, c='blue') #Linha AZUL para as temperaturas Baixas.

# Formata o gráfico
plt.title("death_valley_2014", fontsize=24)
plt.xlabel('', fontsize=16)
#desenha os rótulos com as datas na diagonal para evitar que se sobreponham (falta espaço p/ expor todos).
figura.autofmt_xdate()
plt.ylabel("Temperatura em (F)", fontsize=16)

plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
