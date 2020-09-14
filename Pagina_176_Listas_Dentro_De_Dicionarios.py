# Armazena informações sobre uma pizza que está sendo pedida
'''
#Meu codigo a Baixo, mas me perdi na tradução  :\
pizza = { 'Massa': 'Espessura', 'Cobertura':['Cogumelos','Queijo Extra']}
print('Você Pediu Uma '+pizza['Massa']+ '-Massa Pizza'+'Com os Seguintes Itens')

for recheios in pizza['Cobertura']:
    print('\t'+recheios)
'''

pizza = {
'crust': 'thick',
'toppings': ['mushrooms', 'extra cheese'],} #Pizza é um Dic com uma lista [toppings] dentro
# Resume o pedido
print("You ordered a " + pizza['crust'] + "-crust pizza " +"with the following toppings:")
# Imprimiu O Conteudo da chave Crust & Essas Strings
for topping in pizza['toppings']: # Para o conteudo de pizza Especificamente a Lista Toppings - Que COntém Cogumelos & Queijo Extra ->Que é o que foi mostrado no Print
    print("\t" + topping)

'''Você pode aninhar uma lista em um dicionário sempre que quiser que
 mais de um valor seja associado a uma única chave'''

'''
crust  = Massa
thick = Espessura (Da massa)
toppings = Cobertura (Da Pizza)
'''








