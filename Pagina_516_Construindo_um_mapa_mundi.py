

from pygal_maps_world.maps import World as wd
wm = wd()
wm._title = 'Norte, Centro, Sul'

#add() , que aceita um rótulo e uma lista de códigos de países que queremos destacar.
wm.add('Norte', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
                         'gy', 'pe', 'py', 'sr', 'uy', 've'])
#Tem paises aqui neste add que nao pertencem a Europa, o que define quem aparece no
#..mapa é a sigla dentro da lista. Nada mais.
#SE ABRIR O ARQUIVO.SVG NO NAVEGADOR-> APARECEM TODOS OS PAISES, E EM DESTAQUE OS QUE
#..ESTÃO NA LISTA MENSIONADA  :0  :)
wm.add('Europe', ['ru', 'de', 'fr', 'it', 'jp', 'no', 'sw', 'au', 'gb'])

wm.render_to_file('Americas+.svg')

"""
Cada chamada a add()
define uma nova cor para o conjunto de países e acrescenta essa cor a uma
legenda à esquerda da imagem
"""


'''
#from pygal.maps.world import World
from pygal_maps_world.maps import World
wm = World()
wm.force_uri_protocol = 'http'

wm.title="Map of Central America"
wm.add('North America', {'ca': 84949494949, 'mx': 494794164, 'us': 99794616})

wm.render_to_file('Mapa_Mund.svg')
'''


"""
O METODO DE IMPORTAÇÃO DA APOSTILA NÃO FUNCIONOU. ENTÃO USEI UM SIMILAR ENCONTRADO
NO STACKOVERFLOW, MAS -> ESTA IMPORTAÇÃO NÃO MOSTRA O MAPA DO MUNDO TODO, MAS 
SOMENTE O DOS LOCAIS MENSIONADOS NAS LISTAS DO CODIGO.
"""
