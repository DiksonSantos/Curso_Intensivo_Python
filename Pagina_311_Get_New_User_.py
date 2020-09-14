import json

def Armazenar_nome_usu():
    'Obtém Nome já Existente (Se Houver um já)'
    criar_arquivo_JSON = 'Usuario_P-311.json' #Poderia Estar Vazia ou com '' Que ia funcionar do mesmo Jeito.
    try: #Faça Isso:
        Mensagem = 'Desculpe Arquivo Não encontrado'
        with open(criar_arquivo_JSON) as Objeto_N:
            User_Name = json.load(Objeto_N)
    except FileNotFoundError: #Caso NÃO haja NENHUM Arquivo, Mande o Bloco a Baixo:
        return None #Ou - > Retorne NADA

    else:
        return User_Name #Caso contrario, ou Se -> Houver já algum arquivo, retorne o que estiver carregado em User_Name


def Novo_Nome_Usuario():
    'Pede Novo Nome de Usuario'
    Nome_Usuario = input('Qual se nome? ')
    Nome_Arquivo = 'Usuario_P-311.json'     # MEU ERRO FOI NÃO TER USADO O MESMO NOME DE ARQUIVO .JSON DO DA LINHA 5
    with open(Nome_Arquivo, 'w') as Objeto_Novo:
        json.dump(Nome_Usuario, Objeto_Novo)
    return Nome_Usuario


def Cumprimenta():
    'Cumprimenta Users'
    Nome_Usuario = Armazenar_nome_usu() #Aqui Ele Chama a Função de Cima que é feita Para CRIAR UM ARQUIVO.JASON
    if Nome_Usuario:
        print("Bem Vindo De Volta\t" + Nome_Usuario + '!') #Quando o Arquivo-> Arquivo_P_311_.json Já Existe, Esse Print é Exibido.
    else: #Daqui p/Baixo ele Cria um Arquivo.JSON , Se ele não Existir Para ser CUMPRIMENTADO
        Nome_Usuario = Novo_Nome_Usuario()
        print('Nós Vamos te Lembrar: ' + Nome_Usuario)

Cumprimenta()
'''
def get_stored_username():
    """Obtém o nome do usuário já armazenado se estiver disponível."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Pede um novo nome de usuário."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """Saúda o usuário pelo nome."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("We'll remember you when you come back, " + username+ "!")
    else:
        print("Welcome back, " + username + "!")

greet_user()
'''
