# Armazene os números de 1 a 9 em uma lista
lista = ['1','2','3','4','5','6','7','8','9']

#Percorra a lista com um laço.

for numero in lista:
# Use uma cadeia if-elif-else no laço para exibir a terminação apropriada para cada número ordinal.

    numero = str(numero)
    if numero.endswith('1'):
        print(numero + 'st')
    elif numero.endswith('2'):
        print(numero + 'nd')
    elif numero.endswith('3'):
        print(numero + 'rd')
    else:
        print(numero + 'th')
#cada resultado deve estar em uma linha separada.

#O comando print() já coloca cada resultado em uma linha, bastando usar print() uma vez para cada número, conforme acima.




#COMANDO ENDWITH Muito interessante.
