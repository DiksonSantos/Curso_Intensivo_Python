import requests

# Faz uma chamada de API e armazena a resposta #As 3 Linhas a Baixo São da Página 533:
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
# a var a baixo contem uma função que acessa o endereço www
r = requests.get(url)#A Variavel 'r' contém a requisição da Variavel que contém o Endereço. 'r' é transformada num JSON.
print("Status code:", r.status_code)# = 200 ->Quer dizer que acessou.

#Armazena Resposta da API numa variavel
response_dict = r.json()#
print("Total repositorios:", response_dict['total_count'])


#Explora Informações sobre os repostorios
repo_dicts = response_dict['items']
print("Repositorios Retornados: ", len(repo_dicts))

#Analisa o Primeiro Repositorio
repo_dict = repo_dicts[0]

#Exibimos Varias chaves do "repo_dicts[0]"
print("\nSelected information about first repository:")
print('Name:', repo_dict['name'])
print('Owner:', repo_dict['owner']['login'])
print('Stars:', repo_dict['stargazers_count'])
print('Repository:', repo_dict['html_url'])
print('Created:', repo_dict['created_at'])
print('Updated:', repo_dict['updated_at'])
print('Description:', repo_dict['description'])
"""
print("\nKeys:", len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)
"""
