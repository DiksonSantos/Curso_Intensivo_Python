import csv

nome_arquivo = 'sitka_weather_2014.csv'
with open(nome_arquivo) as Objeto_CSV: #Transformamos num Objeto (qualquer).
    leitor = csv.reader(Objeto_CSV) #csv leitor -> Sabemos que o arquivo é um CSV então Usamos o Leitor Especifico.
    leitor_cru = next(leitor) #-> Isso serve p/ mostrar só o Cabeçalho do Arquivo CSV.
    #print(leitor_cru) #Exibiu o Cabeçalho.

    altos = []
    for cru in leitor:
        Alto = int(cru[1])
        altos.append(Alto) #O numero dentro do [] aqui define Qual Coluna vai ser Lida na Vertical.
    print(altos)

from matplotlib import pyplot as plt
Figura = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(altos, c='red')
plt.xlabel('', fontsize=16)
plt.ylabel("Temperatura em (F)", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.show()
"""
from datetime import datetime
primeira_data = datetime.strptime('2020-04-1', '%Y-%m-%d')
print(primeira_data)
"""
