'''cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
  if car == 'bmw':
    print(car.upper())
else:
    print(car.title())'''

print(80*'==')
sabor = str(input("Sabor Da Pizza: "))
if sabor.lower() == 'milho': #Não Importa se o que foi digitado é maiusculo ou minusculo, o comando LOWER tras pra minusculo e reconhece se for Milho
    print('Temos Aqui')
else:
    print('Sorry Man')

sabor_ = str(input('Digite Outro Sabor: '))
if sabor_.upper() == 'ATUM': #Do mesmo Jeito aqui, mas tudo pra UPPER
    print(' Here it is')
if sabor_ != 'atum':
    print('Vou ficar lhe devendo esta ')

third = str.capitalize(input('Outra OTTA: '))
if third == ('Ameixa'): #Na minha opnião a unica explicação para este codigo estar funcionando é a letra A de Ameixa estar em maiuscula.  :/
    print('Enjoy Mannn!!')
else:
    print('You Got To Wait, forgive us :(  ')

#Estou na PAG 134
