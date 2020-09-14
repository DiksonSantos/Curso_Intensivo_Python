import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

#Faz Uma chamada de API e armazena a resposta
# #Mudando o nome da linguagem no Link a baixo, conseguimos informaações sobre estas linguagens.
pagina = 'https://api.github.com/search/repositories?q=language:python&sort=star'
requisicao = requests.get(pagina)
print("Codigo do Status: ", requisicao.status_code)

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
#modificar os atributos de my_config personalizará a aparência do gráfico:
my_config = pygal.Config()
#Rotação das legendas do Eixo X em 45 Graus:
my_config.x_label_rotation = 45
my_config.show_legend = False
# Tamanho da fonte para o título do Gráfico:
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
#Limita os nomes mais longos para apenas 15 Caracteres:
my_config.truncate_label = 15
my_config.show_y_guides = False
#Largura personalizada para que o gráfico use mais do espaço disponível:
my_config.width = 1000
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on Git Hub'
chart.x_labels = names
chart.add('Uma String+Lista->', stars)
chart.render_to_file('Pag_542.svg')
