'''Informações aninhadas
Às vezes, você vai querer armazenar um conjunto de dicionários em uma
lista ou uma lista de itens como um valor em um dicionário. Isso é
conhecido como aninhar informações.
Podemos aninhar um conjunto de
dicionários em uma lista, uma lista de itens em um dicionário
ou até mesmo
 um dicionário em outro dicionário. Aninhar informações é um
recurso eficaz, como mostrarão os próximos exemplos.'''

#Dicionarios Podem ir Dentro de Listas
#___________________________________________________

'''
#Criando Uma Lista Vazia P Armazenar Aliens:
aliens_ =[]
#Agora criaremos 30 alens verdes:
for alien_number in range(30):
    new_alien = {'Color':'Green','Points':'5','Speed':'Slow'}
    aliens_.append(new_alien)
#Mostrar os 5 Primeiros ALiens:
for alien in aliens_[:5]:
    print(alien)
print('...')
#Total de Aliens Criados
print('Total de Verdinhos: '+str(len(aliens_))) '''
#__________________________________________________________



aliens = []
for alien_number in range(0,30): #Observação -> Antes ele colocou apenas(30)
    new_alien = {'color':'Green','Pontos':'6','Speed': 'Slow'} #Aqui vc pode alterar Yellow ou Green p\ Mudar os resultados do Print
    aliens.append(new_alien)
for alien in aliens[0:5]: #Significa ALterar o Valor dos 3 primeiros da lista Criada pelo IN RANGE
    if alien['color'] == 'Green': # Repare que aqui tem == E Depois apenas =
       alien['color'] = 'Yellow'  # QUer dizer: Se Alien é Green os valores deverão ser substituidos pelos novos valores que tem apenas Um =
       alien['Speed'] = 'Medium'
       alien['Pontos'] = 10
for alien in aliens[3:8]:  #Preciso de mais inf about esses Posicionamentos na Lista
    if alien['color'] == 'Yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
for alien in aliens[0:8]:  #[0:8]
    print(alien)
print('....')

'''Poderíamos expandir esse laço acrescentando um bloco elif que
transforme alienígenas amarelos em alienígenas vermelhos e rápidos, que
valem 15 pontos cada. Sem mostrar o programa todo novamente, esse laço
teria o seguinte aspecto:
for alien in aliens[0:3]:
if alien['color'] == 'green':
alien['color'] = 'yellow'
alien['speed'] = 'medium'
alien['points'] = 10

elif alien['color'] == 'yellow':
alien['color'] = 'red'
alien['speed'] = 'fast'
alien['points'] = 15
'''
