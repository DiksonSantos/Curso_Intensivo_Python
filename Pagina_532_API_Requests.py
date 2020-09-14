import requests

#Faz chamadas de APIs armazenando respostas
Pagina = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
#Faz a Chamada da Variavel que contém o endereço:
r = requests.get(Pagina)
print("Codigo do Status: ", r.status_code)

#Armazena a resposta da API em uma variavel
resposta_dict = r.json()

#Processa o Resultado
print(resposta_dict.keys())

"""
Como o código de status é 200, sabemos que a requisição teve sucesso. O
dicionário com a resposta contém apenas três chaves: 'items' ,
'total_count' e 'incomplete_results' .
"""
#Continua na Pag 533
