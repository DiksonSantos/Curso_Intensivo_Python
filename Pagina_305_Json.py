#Escritor.PY

import json

#num = [ 2,3,5,7,11,13]
#num = ('Dikson Masters')
num = str(input("Digite Algo: "))

nome_arquivo = 'num.json'
with    open(nome_arquivo, 'w') as F_Objeto: #abrimos o arquivo em modo de escrita.
    json.dump(num, F_Objeto) #JSON armazenar a lista num no arquivo numbers.json. (ali em cima).
    

#Leitor.PY

file_name = 'num.json'
with open(file_name) as F_Object:
    numbers = json.load(F_Object)
print(numbers)
