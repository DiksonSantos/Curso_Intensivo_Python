'''
import __Modulo_pizza as P

P.make_pizza(12,"Algodão", "Linhaça")
P.make_pizza(16,"Almondegas","Inhoque","Macarrão Sem Glutém")
P.soma_pizza(2,6)

'''
# import nome_do_módulo as nm
#_____________________________________


#Importando Todas as Funções de Um Modulo:

'''
No entanto, é melhor não usar essa abordagem quando
trabalhar com módulos maiores, que não foram escritos por você:
'''

from __Modulo_pizza import *

make_pizza(12,"Babalu", "Banana")
soma_pizza(30,35)

'''
As
funções devem ter nomes descritivos, e esses nomes devem usar letras
minúsculas e underscores.

EU NÃO SABIAA !
'''

# +
'''
EXEMPLO DE COMO ORGANIZAR UMA FUNÇÃO MUITO LONGA:

def nome_da_função(
        parâmetro_0, parâmetro_1, parâmetro_2,
        parâmetro_3, parâmetro_4, parâmetro_5):  #TAB 2 VEZES
    corpo da função...    #TAB 1 X
'''
