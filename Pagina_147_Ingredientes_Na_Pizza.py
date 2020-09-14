# PEDAÇO DE SOFTWARE QUE TRATARIA DE UMA PIZZA DE COGUMELOS:
'''print( 'Itens Extras Na promoção\t -> Pimentão Verde &',
      'Queijo Extra\n')'''
rec = str.capitalize(input('Escolha o Ingrediente Extra: '))#Itens Extras que o Cliente Pode Pedir a mais.
itens = ['Cogumelos', 'Pimentão Verde', 'Queijo Extra'] #Itens Da Pizza  ->Cogumelos e Pimentão Não tem P/por em Dobro
for recs in rec.upper() and  itens:
    print('Adicionando  ' + recs.upper() + '.')
    if 'Cogumelos' in rec:
        print('Desculpe, Não Temos Cogumelos No Momento')#Se o Cliente pede este Item em dobro, = Não temos mais
if rec.upper() == 'Malagueta':
    print('Desculpe, mas pra que tanta pimenta assim')#Não tem: O Software tenta te convencer de não pegar este em dobro.
for ingr in itens:
    if rec not in itens: # Qualquer Ingrediente diferente dos da lista não estão na Promoção, por isso é emitido um aviso.
        print('Este Ingrediente',itens ,'Não Esta na Promoção, Vai querer??')
print('\nFinalizada Sua Pizza')

# O software a cima não funcionou muito bem, mas ta valendo ^^



#A BAIXO É O SOFTWARE DO PDF:
'''ingreditnes = ['Cogumelos', 'Pimentão Verde', 'Queijo Extra']

for ingrediente in ingreditnes:
    if ingrediente == 'Pimentão Verde':
        print('Desculpe Acabou A Pimenta :/   .')
    print('Adicionando  ' + ingrediente + '.')
print('\nTerminamos de Fazer Sua Pizza')'''



#Continuar na 148 
