import requests

Pagina = 'https://api.github.com/rate_limit'
R = requests.get(Pagina)
JSON = R.json()
print(JSON["resources"])


for chave, valor in JSON.items():
    for V, C in valor.items():
        if V == "limit":
            print(V, C)
"""
item = chave + valor
key = chave
value = conteudo da chave ou valor.
"""
