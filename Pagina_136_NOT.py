usu = str.capitalize(input("Digite Seu Nome: "))
banidos = ['Aurora', 'Aninha','Elis']
banidos.append('Mary')
expulsos = ('Bet', 'Marcy')
if usu in banidos or usu in expulsos: #Adicionoei o OR para incluir a TUPLA Expulsos
    print(usu.title() + ' ,Você Foi Banida! Chau e bença ')
if usu not in banidos and usu not in expulsos:
    print(usu.title()+' ,Yor´re Still in')
print(usu.capitalize() and usu.title() == 'Gow') #Este codigo mostra FALSE ou TRUE na tela de acordo com ...
print(70*'=')

#Estou em PAG 137
