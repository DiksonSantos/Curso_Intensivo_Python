"""
from pygal_maps_world.maps import WORLD_MAP
WM = WORLD_MAP()
"""

from pygal_maps_world.maps import World as wd
WM = wd()


WM.title = 'População dos Paises na America do Norte e do Sul'

"""Quando só quiser mensionar o pais-> Use [] , Quando quiser atribuir um numero
a cada um deles, use {} Dicionarios """
WM.add('America do Norte', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})

WM.add('America do Sul', {'br': 20926000, 'ar': 40895751})

WM.render_to_file('North_Pop_+SulAmerica.svg')


"""
MELHOR OPÇÃO PARA ABRIR ESTES ARQUIVOS .SVG É COM NAVEGADOR FIREFOX

-> QUANDO VOCE PASSAR COM O PONTEIRO DO MOUSE OR SOBRE OS PAISES ELE MOSTRA A 
POPULAÇÃO TOTAL DESTE.

-> QUANTO MAIS ESCURO O PAIS, MAIS POPULOSO ELE É. 


"""


#CONTINUA NA PAG 519
