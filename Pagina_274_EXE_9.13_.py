"""
#9.13 Reescrevendo o programa com OrderedDict:
from collections import OrderedDict

glossario = OrderedDict

glossario = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
    'key': 'The first item in a key-value pair in a dictionary.',
    'value': 'An item associated with a key in a dictionary.',
    'conditional test': 'A comparison between two values.',
    'float': 'A numerical value with a decimal component.',
    'boolean expression': 'An expression that evaluates to True or False.',
    }

for word, defi in glossario.items():
    print("\n" + word.upper() +": " + defi.title())

#OK
"""

#9.14 Dados:

from random import randint

x = randint(1, 6)

class Die():
    def __init__(self, sides=6):
        self.Lados = sides #Sides -> Var interna que recebe o Atributo especificado no Objeto

    def roll_die(self):
        #print(x)
        return randint(1, self.Lados) #Este metodo retorna um RandInt + o valor que for colocado em Sides

# Make a 6-sided die, and show the results of 10 rolls.
D6 = Die() #Não foi especificado Valor, então por default é 6 -> Objeto vai funcionar com Metodo da Classe DIE

results = [] #Lista vazia
for roll_num in range(10): # Executa 10x
    result = D6.roll_die() #Resultado = Objeto com Metodo que Randomiza numero 6 Vezes
    results.append(result) #Lista vazia - Recebe results que Contém o Objeto D6 que esta com o Metodo rodar Dado
print("Dez Rodadas de um Dado de 6 Lados:")
print(results) #Aqui é a Lista que estava Vazia e Recebeu o Objeto com o Metodo que Randomizou o Numero.

#_____________________________________________

D20 = Die(sides=20) #A Classe Die contém o metodo principal que trabalha com um atributo que recebe um numero. Só isso.

Resultado = []
for rodar_num in range(10): #Quantidade de vezes(Rodadas) que o Codigo identado a baixo vai ser Executado.
    Resultado_T = D20.roll_die() #Variavel recebe 20x o objeto com o metodo que randomiza
    Resultado.append(Resultado_T) #Acrescenta Resultado_T á Resultado.
print("\nDado de 20 lados -> 10 Rodadas") #Espe print esta fora do laço FOR então só é executado 1x.
print(Resultado)
#__________________________________________________

D30 = Die(sides=30)

Resultado_3 = []
for roda in range(11):
    Res_Q = D30.roll_die() #Na verdade neste trecho aquie ele esta recebendo 30 (Dentro do parenteses)
    Resultado_3.append(Res_Q)
print("\nDado de 30 lados -> 11 Rodadas")
print(Resultado_3)

#Continua na PAG-278

