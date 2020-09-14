#8.15 – Impressão de modelos:

#Já testei isso Mas sem Usar estas Funções Bostas Lixo Confusas. A ideia é a mesma, Fiz com outra, funcionar.



#'''
#8.16 Importações:

import __Modulo_pizza
'''
from __Modulo_pizza import make_pizza

#Função(Tamanho, Recheo, Outro_Recheio)
make_pizza(12, "Peperoni", "Nabu")

from __Modulo_pizza import  soma_pizza

soma_pizza(32, 1)

from __Modulo_pizza import  make_pizza as mp

mp(18,"Alface")

import __Modulo_pizza as nm

nm.make_pizza(12,"Mandioca", "Maionese")
nm.soma_pizza(1,3)
'''
from __Modulo_pizza import *
soma_pizza(1,6)
make_pizza(13,"Cogumelos","Jaca Salgada")

'''
Quando for necessário modificar o
comportamento de uma função, basta modificar apenas um bloco de
código e sua alteração terá efeito em todos os lugares em que uma
chamada dessa função for feita.
'''








