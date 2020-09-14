print(80*'=','\n Insira os ingredientes A baixo:')
print('\n Cogumelos, Queijo Extra, Milho Verde\n')
ins = str.title(input('Digite Seus Ingredientes->_ '))

if 'Cogumelos'in ins:
    print('Cogumelos Adicionados',ins.upper())
if 'Queijo Extra' in ins:
    print('Adicionado Queijo Extra')
if 'Milho Verde' in ins:
    print('Adicionado Milho Verde')

print('Pizza Terminada com Ingredientes -> ', ins.upper())

'''Neste Software, se varias condições forem tidas como TRUE, todas 
elas serão mostradas, graças ao uso do IF,se tivéssemos usado um
bloco IF-ELIF-ELSE, o código pararia de executar depois que apenas um
teste tivesse passado (TRUE).'''
