current_number = int(input('Digite Um Numero: '))
while current_number <10:
    current_number += 1
    if current_number % 2 == 0: #Se Current_Number tiver Resto =  0 Continue
        continue
    print(current_number)

'''
Para todo numero em current_number Menor Que 10 e que For Divisivel Por 2 Com Resto 0
Ele continua adicionando 1 e Exibindo no Print 

O Curioso é que ele não esta mostrando os Numeros que Tem Divisão Com Resto 0
Mas sim só os Impares, ou com resto de divisão (!=) de 0
'''
