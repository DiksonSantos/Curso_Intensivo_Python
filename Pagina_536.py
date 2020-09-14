"""
Na pagina 533 ele estava trabalhando somente com as informações da posição ZERO, já nesta criamos um laço FOR para
percorrer todas a sposições e mostrar suas informações:
"""

import requests

# Faz uma chamada de API e armazena a resposta #As 3 Linhas a Baixo São da Página 533:
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
# a var a baixo contem uma função que acessa o endereço www
r = requests.get(url)#A Variavel 'r' contém a requisição da Variavel que contém o Endereço. 'r' é transformada num JSON.
print("Status code:", r.status_code)# = 200 ->Quer dizer que acessou.

#Armazena Resposta da API numa variavel
response_dict = r.json()#Transformou as informações da Pagina Num Arquivo JSON
print("Total repositorios:", response_dict['total_count'])


#Explora Informações sobre os repostorios
repo_dicts = response_dict['items']
print("Repositorios Retornados: ", len(repo_dicts))#Aparece 30x {} na folha\Pagina.

#Analisa o Primeiro Repositorio
#repo_dict = repo_dicts[0]

print("\nSelecionadas as informações sobre Cada Repositorio:")
for repo_dict in repo_dicts:
    print('\nName:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print('Description:', repo_dict['description'])

