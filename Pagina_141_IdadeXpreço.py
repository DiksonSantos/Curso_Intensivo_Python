age = int(input('Digite Sua Idade: '))
if age <4:
    price = 0
elif age <18:
    price = 5
elif age <65:
    price = 10
    print('Vai Jogar Bingo vôvô')
elif age <75:
    price = 00,'Free'
    print('Go Home Dearest')
else:
    price = 5
print('Your Admission Cost is ' + str(price)+ '$.')
'''Para mudar o texto da mensagem de saída, seria necessário alterar
  apenas uma instrução print, e não três instruções print sepadas.'''


#pag 143
