#Pizza

disponivel = ['Cogumelos','Azeitonas','Pimentão Verde','Peperoni','Abacaxi','Queijo Extra']

requisitados = ['Cogumelos', 'Batata Frita','Queijo Extra'] #Pedidos pelo cliente

for requisitado in requisitados:
    if requisitado in disponivel:
        print('Adicionando\t'+ requisitado + '.')
    else:
        print('Desculpe, Nos Não Temos\t'+ requisitado+'.')
print('\nTerminamos de Fazer Sua Pizza!')



# As tentativas de Software A baixo Não funcionaram :/
'''pedido = str.title(input('Digite o Item: '))

disponivel = ['Cogumelos','Azeitonas','Pimentão Verde','Peperoni','Abacaxi','Queijo Extra']
if pedido ==disponivel:
    print({},'Item Disponivél '.format(pedido))
else:
    print('Não Temos Este Item')
str.title(input('Digite Um Item: '))
for Item in range(len(disponivel)):
    if pedido == disponivel[Item]:
        print(pedido, 'Sendo Adicionado')
        break
else:
    print(pedido,' Sendo Acrescentado a Sua Pizza')'''





'''if requisitados in disponivel:
        print('Adicionando\t'+ requisitado + '.')
    else:
        print('Desculpe, Nos Não Temos\t'+ requisitado+'.')
print('\nTerminamos de Fazer Sua Pizza!')'''
