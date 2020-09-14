"""
import json
from Pag_514_Country_Codes import  pega_cod_pais
from pygal_maps_world.maps import World as wd
WM = wd()

#Carrega de uma lista

nome_arquivo = 'population_data.json'
with open(nome_arquivo) as FU:
    dados_pop = json.load(FU)

# Exibe população de cada pais em 2010
for pop in dados_pop:
    if pop['Year'] == '2010':
        nome_pais = pop['Country Name']
        populacao = pop['Value']

#Constroi um dicionario com dados das populacoes
cc_pop = {}
for pop_dic in dados_pop:
    if pop_dic['Year'] == '2010':
        pais = pop_dic['Country Name']
        populacao = int(float(pop_dic['Value']))
        codigo = pega_cod_pais(pais)
        if codigo:
            cc_pop[codigo] = populacao

WM._title = 'População Mundial em 2010, por País'
WM.add('2010', cc_pop)
WM.render_to_file('Pagina_519_20_População Mundial.svg')
"""

import json
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS
from pygal_maps_world.maps import World as WD
#from pygal_maps_world.maps import *
from Pag_514_Country_Codes import pega_cod_pais

# Load the data into a list.
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# Build a dictionary of population data.
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = pega_cod_pais(country_name)
        if code:
            cc_populations[code] = population

# Group the countries into 3 population levels.
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}

for cc, pop in cc_populations.items():
    # 85 Paises
    if pop < 10000000: #Guarda Paises com Até este numero
        cc_pops_1[cc] = pop
    # 70 Paises
    elif pop < 1000000000: #Guarda Paises com Até este numero -> que é um pouco maior q o anterior.
        cc_pops_2[cc] = pop
    else:
    # 2 Paises:
        cc_pops_3[cc] = pop
    #print(f"CC={cc} Pop={pop}") cc-> EUA ou BR por Exemplo. pop-> Numero de Habitantes.

# See how many countries are in each level.
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))
"""
Essa saída mostra que há 85 países com menos de 10 milhões de pessoas,
69 países com população entre 10 milhões e 1 bilhão de pessoas e dois
países extremos com mais de 1 bilhão.
"""
from pygal.style import LightColorizedStyle as LG
dc = {'ca'}
wm_style2 = LG
wm_style = RS('#336699', base_style=LCS)
#wm = pygal.Worldmap(style=wm_style) #NÃO FUNCIONA MAIS ATUALMENTE.
#wm = wm(style=wm_style) #GAMBIARRA QUE EU FIZ, MAS TAMBÉM NÃO SURTIU O EFEITO ESPERADO.
wm = WD(style=wm_style2)
#wm.force_uri_protocol = 'http'
wm.title = 'World Population in 2010, by Country'
#Aqui Iluminou a America Do Norte toda. O problema é que; estes .adds NÃO estão recebendo Estes dicionarios 'cc_pops_2'
#wm.add('0 a 10', ['ca', 'mx', 'us'])
wm.add('0-10m', cc_pops_1)  #Se eu colocar a Var 'dc = {'ca'}' .Funciona. Mas cc_pops NÃO.
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('Pagina_519_20_População Mundial.svg')

"""
Não Obtive os mesmos Resultados dos mostrados no Livro, pois, o método de Import
mostrado no livro esta ultrapassado. E o metodo atual não obtive a mesma reação.
"""
#Soluções dos Exercicios:
#https://ehmatthes.github.io/pcc/solutions/chapter_16.html
