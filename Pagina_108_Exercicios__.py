# 4.1
'''pizzas = ['milho','marguerita','queijo','napolitana']
for p in pizzas:
    print('As Melhores São As Vegetarianas:',p.title() ,'Bom Apetite')'''

#4.2
'''alcateia = ['Lobo Guará','lobo da Etiópia', 'lobo cinzento','lobo vermelho']
for woulf in alcateia:
    print(woulf.title()+ '  Aaaauuuuullllll')
print('Existem três espécies de lobos : o lobo vermelho (Canis rufus), o lobo da etiópia\n (Canis simensis) e o lobo cinzento (Canis lupus). Segundo alguns \nautores, esta última espécie pode ser subdividida em cerca de 30 subespécies,\n entre as quais se encontra o lobo ibérico (Canis lupus signatus).')
'''




#Pagina 111:
'''squares =[]
for value in range(1,11):
    square = value**2
    squares.append(square) # Traduzindo --> value vai de 1 a 10. square é = os valores de value ao quadrado.
#squares (que era a lista vazia) recebe o valor de Square.
print(squares)'''

#Ou:
'''squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)'''

#Pag 112  Bem mais simples ;
'''squares = [value**2 for value in range(1,11)]  #Lista Compreenção
print(squares)'''

'''#4.3  Pagina 113:
for value in range(0,21):
    print(value) # Imprime Valores de 0 a 20 cada valor por linha'''

'''#4.6 Numeros Impares
numb = list(range(1,22,2)) #Imprime de 1 até 21 de 2 em 2
print(numb) '''

#4.7
'''mult_3=[list(range(3,31,3))]
print(mult_3)'''

#4.8:  Não sei se acertei ... mas
'''lista=[]
for valor in range (1,10,1):
    lista.append(valor**3)
    print(lista)'''

#4.9
'''cubos =[valor**3 for valor in range(1,10,1)]       #Outra Lista compreenção;
print(cubos)'''
