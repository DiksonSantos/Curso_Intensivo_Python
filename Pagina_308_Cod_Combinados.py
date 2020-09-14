'''
Carrega o nome do usuário se foi armazenado anteriormente
Caso contrário, pede que o usuário forneça o nome e armazena essa informação
'''

import json
#Testei 'Guarda_Nome_308.json' & 'Guarda_Nome_308.txt'  Os Dois funcionam...
nome_arquivo = 'Guarda_Nome_308.txt' #Caso o Aqrquivo Aqui Esteja Limpo, o Programinha te pergunta seu nome.
try: #Tente ler o Arquivo JSON, caso ele esteja limpo, Sera rodado o que estiver a Baixo de "Except".
    with open(nome_arquivo) as Objeto_F: #Se esse arquivo tiver algo escrito.
        Nome_Usuario = json.load(Objeto_F) #lemos o nome do usuário de volta para a memoria
#Se o Bloco With der errado ou seja, o arquivo estiver limpo:
except FileNotFoundError: #Na verdade aqui, não 'Roda' quando ele não encontra arquivo, mas sim quando o mesmo esta Limpo.
    Nome_Usuario = input('Nome? ') #..ele te pergunta um nome.
    with open(nome_arquivo, 'w+') as Objeto_F: #Cria o Arquivo com o w+
        json.dump(Nome_Usuario, Objeto_F) #Então o json.dump() pega a informação que foi digitada na Variavel, e joga para o Objeto JSON
        print('Nós Vamos Te Lembrar Quando Você Voltar, ' + Nome_Usuario)
#Caso ele abra e leia o arquivo com o 'with' e não precise rodar o 'except', o 'else' roda apresentando o resultado do 'with'.
else: #Neste caso o 'Nome_Usuario' é a linha 'json.load' que carregou o arquivo 'txt' ou 'json'.
    print("Bem Vindo De volta " + Nome_Usuario) #Se O Arquivo ('username.json') Já Existir Ou Se já Estiver Escrito, Ele Printa Isso
