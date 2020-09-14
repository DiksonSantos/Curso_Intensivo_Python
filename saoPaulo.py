import csv


SP = 'SaoPauloTRY1954_05.csv'
with open(SP, encoding="latin-1") as OBJ:
    X = csv.reader(OBJ, delimiter=',')
    for coluna in X:
        print(coluna)
