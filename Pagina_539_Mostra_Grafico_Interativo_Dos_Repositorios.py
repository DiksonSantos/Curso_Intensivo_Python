import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

#Faz Uma chamada de API e armazena a resposta
# #Mudando o nome da linguagem no Link a baixo, conseguimos informaações sobre estas linguagens.
pagina = 'https://api.github.com/search/repositories?q=language:fortran&sort=star'
requisicao = requests.get(pagina)
print("Codigo do Status: ", requisicao.status_code)
"""
# Armazena Resposta e uma API numa variavel
resposta_dicio = requisicao.json()#Agora que transformamos a pagina num JSON podemos usar laços FOR etc...
print("Total de Repositorios:", resposta_dicio['total_count'])

#Explora informações sobre o repositorio:
repo_dicts = resposta_dicio['items']

nomes, estrelas = [], []
for repo_dict in repo_dicts:
    nomes.append('name')
    estrelas.append('stargazers_count')

#Criar Visualizaçao:
meu_estilo = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=meu_estilo, x_label_rotation=45, show_legend=False)
chart.title = 'Maior Quantidade de Estrelas em Projetos Python no GitHub'
chart.x_labels = nomes
chart.add('', estrelas)
chart.render_to_file('Pagina_539.svg')
"""


# Armazena a resposta da API em uma variável
response_dict = requisicao.json()
print("Total repositories:", response_dict['total_count'])

# Explora informações sobre os repositórios
repo_dicts = response_dict['items']
names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# Cria a visualização
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Maior Quantidade de Estrelas em Projetos Python no GitHub'
chart.x_labels = names
#A quantidade de estrelas esta no Eixo Y:
chart.add('Nome:', stars)#Quando aponta o mouse nas barras ele mostra Isto.
chart.render_to_file('Pagina_539.svg')

