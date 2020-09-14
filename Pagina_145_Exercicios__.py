''''#Exer 5.3
print(70*'=')
print('Escolha Uma das 3 cores -> Green, Yellow ou Red')
cor = str.title(input('Escolha Uma Cor->_ '))
if cor == 'Green':
    pontos = 5
elif cor == 'Yellow':
   pontos = 1
elif cor == 'Red':
    pontos = 2
else:
    pontos = 00
    print('Cor Não Consta')
print('Você Conseguiu', str(pontos),'Pontos')'''

#5.7 Fruta Favorita
frutas = ['maçã', 'pera', 'melancia','mamão']
if 'maçã' in frutas:
    print('Fruta Vermelha na Lista')
if 'pera' in frutas:
    print('Fruta Verdinha na Lista')

insert = str.title(input('Qual Sua Fruta Favorita?? '))
print('Você Realmente gosta de', insert, '???')

if 'melancia' in frutas:
    print('Esta é Pesada')
if 'mamão':
    print('Bom pra fazer um Nº2 mais tarde')

#continua na Pagina 147 Pizza
