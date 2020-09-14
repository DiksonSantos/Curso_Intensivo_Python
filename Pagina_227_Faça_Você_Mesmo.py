magicos = ['Magico de Oz','Mister Magu','Magic Raul','Mestre dos Magos']

#8.9
def show_magicians(magicians): #Esta é uma Variavel Local que esta interligada apenas com a que esta Dentro desta função
    """Print the name of each magician in the list."""
    for magician in magicians: #Apesar de poder ter o mesmo nome da lista de fora da função, elas Não Estão Interligadas.
        print(magician.title())

magics = ['harry houdini', 'david blaine', 'teller']
#show_magicians(magicos)
#print("\n")
#show_magicians(magicos)


'''
Resumindo. Esta é Um tipo de função Criada Especificamente Para trabalhar com Listas MAGICIANS da linha DEF é um exemplo
de uma lista, Mas as que na verdade Vão ser Usadas são as listas de fora da Função. Inseridas entre () do chamado da função.

Se eu for criar Uma função para calcular Numeros, ela tem que ter um exemplo ou amostra de calculo interno, para ela 
'Saber' dos proprios mecanismos. Exatamente Como A baixo;
'''

'''
def calcula(Numero, Numeral):
    Resultado = Numero + Numeral
    print(Resultado)
Numero = int(input('Numero: '))
Numeral = int(input("Numero++: "))

calcula(Numero,Numeral)
'''

'''
#8.10;
def show_magicians(magicians):
    """Print the name of each magician in the list."""
    for magician in magicians:
        print(magician)  #Acho que esta é uma função que imprime listas, Um item Por linha.

def make_great(magicians_): #Devemos ver esta variavel local como ELEMENTO que vai receber as informações de algo externo (Como Uma Lista por exemplo).
    """Add 'the Great!' to each magician's name."""
    # Build a new list to hold the great magicians.
    great_magicians_LIST = []

    # Make each magician great, and add it to great_magicians.
    while magicians_: #Enquanto Houver Itens Na Lista ele executa o laço a abixo.
        magician = magicians_.pop() #MAGICIAN Recebe o que for extraido do Elemento Externo (Ou Lista)
        great_magician = magician + ' THE GREAT' #Faz a Fusão de cada Um dos Itens de MAGICIAN com a String ''
        great_magicians_LIST.append(great_magician) #Great_Magicians -> Recebe a Lista Concatenada\Fundida (APPEND) ->Esta Nova Variavél Recebe a Lista.
        #Nesta Linha com as tres de Cima esta o Esquema Cavernoso!
#Passo 1 ->EXTRAI | Passo 2 -> MODIFICA | Passo 3 -> ARMAZENA Numa Nova Lista o Produto\Elemento Alterado.


    # Add the great magicians back into magicians. Ou -> Adiciona o Produto Final de Volta na Primeira Lista (Que é a Variavel Local do Cabeçalho da Função).
    for great_magician in great_magicians_LIST: #Vai Pegar Os Itens da Lista GREAT MAGICIANS que Recebeu GREAT MAGICIAN e;
        Magicians.append(great_magician)  #Com o APPEND devolve-los á variavel Local do Cabeçalho.

Magicians = ['Harry Houdini', 'David Blaine', 'Teller']

show_magicians(Magicians) #É ADD á Função a lista, que é Modificada pelas 3 linhas Internas da Função, Devolvida á Variavel do Cabeçalho,

print("\n")

make_great(Magicians)   #Esta função transforma. Ela vem ANtes

show_magicians(Magicians)
#Esta Função Imprime. Por Isso Ela vem Depois. Esta Foi Chamada De novo DEPOIS da MAKE_GREAT, Assim ela Imprime O Conteudo TRANSFORMADO Pela Make_Great
'''

#8.11 Mágicos Inalterados:
'''def mostre_magicos(Magicos):
    for magico in Magicos:
        print(magico)

def fazer_grande(magicos):
    Grandes_Magicos = []


    while magicos:
        magico = magicos.pop #Magico Representa os elementos (singulares) Da Lista\Elemento de Entrada.
        grandes_magicos = magico + 'O Grande'   #grande magico é uma Variavel Local. Que Recebeu cada Item da Lista de Entrada concatenado com "O Grande"
        grandes_magicos.append(grandes_magicos) #É a Lista, recebendo a vcariavel Local ->Esta Linha só serve para guardar o que foi feito nas Duas Linhas de Cima.

#O FOR Adiciona a Lista Grandes_Magicos em magicos (Que é a variavél Da Função)
    for grande_magico in Grandes_Magicos: #grande_magico vai percorrer a Lista Grandes_Magicos
        magicos.append(grande_magico) #Os itens percorridos Vão ser Guardados em grande_magico

    return magicos # Torna acessivel o conteudo da variavel Da Função.

magicos = ['Harry Houdini', 'David Blaine', 'Teller']

mostre_magicos(magicos)

print("\n Os Grandes Magicos ->  ")

grandes_magicos_ = fazer_grande(magicos[:])


mostre_magicos(grandes_magicos_)

print("\nLista Original")

mostre_magicos(Magicos)

#_________________'''

#8.11
def show_magicians(magicians): 			#Função Para Imprimir\Mostrar
    '''Print the name of each magician in the list.'''
    for magician in magicians:
        print(magician)

def make_great(magicians):  			#Função Para Armazenar os Itens da Lista
    '''Add 'the Great!' to each magician's name.'''
    # Build a new list to hold the great musicians.
    great_magicians = []

    # Make each magician great, and add it to great_magicians. 
    while magicians:				#Enquanto houver itens na lista, faça os procedimentos a baixo.
        magician = magicians.pop()		#Tirou da Lista de Entrada (Magicians), Colocou em MAGICIAN
        great_magician = magician + ' THE GREAT' #Guardou MAGICIAN em GREAT_MAGICIAN , e Dentro desta Ultmi, Fez a Concatenação
        great_magicians.append(great_magician)  # GREAT MAGICIANS Que Era a Lista VAZIA Criada Ali Em Cima, Recebe GREAT_MAGICIAN  Que Contem os Itens Concatenados.

    # Add the great magicians back into magicians.
    for great_magician in great_magicians: 	# Percorre a EX Lista Vazia
        magicians.append(great_magician)	#Devolve a EX Lista Vazia para a Variavél Interna da Função (Que P| Fuder c\ td tem o mesmo Nome do Parametro da função

    return magicians				#Retorna a Ultima VAR Com as Infs Transformadas 

magus = ['Harry Houdini', 'David Blaine', 'Teller']
'''print("Original List".upper())
show_magicians(magus)'''

print("Great Magicians With Copied List:".upper())
great_magicians = make_great(magus[:])
#Esta função recebe a var a cima que esta com Outra função que possui uma copia da lista 'magus[:]'
#..a qual alterou todos os itens da lista concatenando-os con Strings 'Great'.
show_magicians(great_magicians) #Essa aqui só mostra o que a 'Make_Great' fez com uma cópia da Lista.

print("\nOriginal Magicians:".upper())
show_magicians(magus)# E essa aqui mostra a original.


