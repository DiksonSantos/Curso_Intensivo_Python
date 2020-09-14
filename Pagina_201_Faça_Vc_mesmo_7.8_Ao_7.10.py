'''# 7.8 Lanchonete:
Pedidos_De_Sanduiches = ['Lentilha','soja','jaca','Abobora']
Finalizados = []

while Pedidos_De_Sanduiches:
    Prontos = Pedidos_De_Sanduiches.pop()

    print('Preparei Seu Sanduiche de '+Prontos.title())

    Finalizados.append(Prontos)


print('Os Seguites Lanches Já Estão Prontos:')
for Finalizado in Finalizados:
    print(Finalizado.title())

#Ual !!!! COnsegui !!!!!!!!
'''
#____________________________________________________________________


#7.9 Sem Pastrami (Seja la o que for isto)
'''
Pedidos_De_Sanduiches = ['Lentilha','soja','jaca','Abobora','Pastrami']
Finalizados = []
print('Desculpe, Não Temos '+Pedidos_De_Sanduiches[4])
while 'Pastrami' in Pedidos_De_Sanduiches:
    removido = Pedidos_De_Sanduiches.remove('Pastrami')



while Pedidos_De_Sanduiches:
    Prontos = Pedidos_De_Sanduiches.pop()

    print('Preparei Seu Sanduiche de '+Prontos.title())

    Finalizados.append(Prontos)


print('Os Seguites Lanches Já Estão Prontos:')
for Finalizado in Finalizados:
    print(Finalizado.title())
#print(Finalizados[4]) # O elemento PASTRAME não esta em Nenhum Indice desta Lista (Finalizados)
'''
#____________________________________________________________________________

#7.10 -> Ferias Dos Sonhos:
Respostas = {}
Flag_Ativa = True
for Pess in range (1,3): #COm o FOR Ele Exibe todos os resultados assim que (neste caso) as duas pessoas tiverem Respondido
#while Flag_Ativa:  #Com o WHILE ele mostra os resultados a cada vez que uma pessoa responde as perguntas.
    print('Insira Seu Nome e Digite ENTER: ')
    Nome = input('Nome: ')
    Local = input('Para Onde Gostaria de Ir? ')
    Respostas[Nome] = Local
    Repetir = input('Outra Pessoa\Local ?? (Sim/Não)? ')
    if Repetir == 'Não':
        Flag_Ativa = False
    print('Aqui Estçao Os Resultados:')
    for Nome, Local in Respostas.items():
        print(Nome+' Gostaria de Ir Para: '+Local)

#Ok I think We Did IT !
