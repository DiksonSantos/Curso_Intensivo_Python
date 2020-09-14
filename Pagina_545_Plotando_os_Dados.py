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

print("Number of items:", len(repo_dicts))
names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])


plot_dict = {
    'value': repo_dict['stargazers_count'],
    'label': repo_dict['description'],
}
plot_dicts.append(plot_dict)


# Cria a visualização
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Maior Quantidade de Estrelas em Projetos Python no GitHub'
chart.x_labels = names
chart.add('', plot_dicts)
chart.render_to_file('Pag_545.svg')
