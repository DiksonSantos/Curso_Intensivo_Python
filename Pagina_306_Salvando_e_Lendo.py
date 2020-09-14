import json

# -> Aqui Esse Blocos SÓ funcionam Separados. No Proximo Arquivo serão combinados.

'''
#Meu Codigo:

nome_Usuario = input("Qual Seu Nome? ")

nome_arquivo = 'nome_arquivo.json'
Var = open(nome_arquivo, 'w')
json.dump(nome_Usuario, Var) #DUMB -> Armazena/Escreve arquivo. Em Var que por sua vez contém a Variavel que Contem o arquivo.JSON
print(nome_Usuario) #Agora nome_usuario Contém

'''
'''
#Este é o codigo da Apostila.
username = input("What is your name? ")

filename = 'username.json'
with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print("We'll remember you when you come back, " + username + "!")
'''

nome_arquivo = 'nome_arquivo.json'
with open(nome_arquivo) as Objeto___:
    Usuario = json.load(Objeto___)
    print('Bem Vindo de Volta ' + Usuario + '!')
