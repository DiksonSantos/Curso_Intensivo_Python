import json
from Pag_514_Country_Codes import pega_cod_pais
from pygal_maps_world.maps import World as wd


#Carrega os Dados Numa Lista:
nome_arquivo = 'population_data.json'
with open(nome_arquivo) as Objeto:
    pop_data = json.load(Objeto) #Load Converte o JSON para uma Lista.


# Constrói um dicionário com dados das populações
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = pega_cod_pais(country)
        if code:
            cc_populations[code] = population
"""
wm = wd()
wm.title = 'População Mundial em 2010 por País'
wm.add('2010', cc_populations)

wm.render_to_file('Pagina_519.svg')
"""

"""
ESTA COMPLETAMENTE OK (SEGUNDO OS PADRÕES DE
 IMPORTAÇÃO ATUIAIS DE BIBLIOTECAS), MAS MESMO ASSIM
 NADA DE FUNCIONAR.
"""
