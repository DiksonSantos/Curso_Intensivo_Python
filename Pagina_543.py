import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

meu_estilo = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=meu_estilo, x_label_rotation=50, show_legend='Legendas')

chart.title = 'Projetos Python'
chart.x_labels = ['httpie', 'django', 'flask']

plot_dicts = [
{'value': 16101, 'label': 'Description of httpie.'},
{'value': 15028, 'label': 'Description of django.'},
{'value': 14798, 'label': 'Description of flask.'},
]

chart.add('', plot_dicts)
chart.render_to_file('Pagina_543.svg')
"""
O Pygal
usa o número associado a 'value' para descobrir a altura que cada barra
deve ter, e utiliza a string associada a 'label' para criar a dica de contexto
de cada barra.
Por exemplo, o primeiro dicionário em v criará uma barra
que representa um projeto com 16.101 estrelas, e sua dica de contexto
conterá Description of httpie (Descrição de httpie).

O método add() precisa de uma string e de uma lista.
"""
