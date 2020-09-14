
'''Usuarios = ['Andinho', 'Almeida','Toinho','Fontanelli','Barnabé','Admin']
for Users in Usuarios:
	if 'Admin' in Usuarios:
		print('Olá admin, gostaria de ver um relatório de status?')

Usuarios = ['Andinho', 'Almeida','Toinho','Fontanelli','Barnabé','Admin']
for Ad in range(len(Usuarios)):
	if 'Admin' == Usuarios[Ad]:
		print('Olá admin, gostaria de ver um relatório de status?')

#print('Olaa',Usuarios[0:5], 'Obrigado Por Fazer Login' )


Usua2 = ['Andinho', 'Almeida','Toinho','Fontanelli','Barnabé']
for index in  (Usua2):
	#print(index[0:5],'Ola obrigado por fazer login novamente')     #Acidentalmente com [0:5] em frente index, ele só imprime as 5 primeiras letras de cada nome

	#print(index,'Ola obrigado por fazer login novamente')
	print(Usua2)

#__________________________
Usuarios = ['Andinho', 'Almeida','Toinho','Fontanelli','Barnabé','Admin']
for user in Usuarios:
	print('ola', user,'obrigado por fazer login novamente.')
if 'Admin' in Usuarios:
	print('Olá admin, gostaria de ver um relatório de status?')
#________________________________
print('Loging',50*'=')
Log = str(input('Digite Seu Nome: '))
Usuarios = ['Andinho', 'Almeida','Toinho','Fontanelli','Barnabé']
if Log == Usuarios:
	print('Olá\t',Log,'\tobrigado por fazer login novamente.')
else:
	print('Usuario Não Cadastrado')'''
nome= str.title(input('Digite Seu Nome Para Login: '))
Usuarios = ['Andinho', 'Almeida','Toinho','Fontanelli','Barnabé']
Gestores =['Admin', 'Dono','Mano']
for Usu in range(len(Usuarios)):
	if nome == Usuarios[Usu]:
		print('Olá','{}, Muito Obrigado Por Logar Novamente'.format(nome))
		break
for Usu in range(len(Usuarios)):
	if nome =='Admin' or nome in Gestores:
		print('Olá','{} Administrador, Gostaria de ver o Relatorio?'.format(nome))
		break
for Usu in range(len(Usuarios)):
	if nome not in Usuarios and nome not in Gestores:
		print('Nome Não Consta no Sistema')
		break
	if nome == '':
		print('No Users')
