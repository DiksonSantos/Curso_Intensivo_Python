'''
#10.11 Numero Favorito:
import json
Nome = input("Qual Seu Numero Favorito: ")
Var = 'Numero_Favorito.json'
with open(Var, 'w') as Objeto_Escreve:
    json.dump(Nome, Objeto_Escreve)

def retornar():
    Var = 'Numero_Favorito.json'
    with    open(Var) as Objeto_Read:
        Guard = json.load(Objeto_Read)
        print('Seu Numero Favorito é: ',Guard)
    return Guard

retornar()
#OK WE DID IT !!!
'''

'''
#10.12 Lembrando Numero Favorito:
import json
try:
    Var = 'Numero_Favorito.json'
    with    open(Var) as Objeto_Read:
        Guard = json.load(Objeto_Read)
        print('Seu Numero Favorito é: ',Guard)

except FileNotFoundError:
    Nome = input("Qual Seu Numero Favorito: ")
    Var = 'Numero_Favorito.json'
    with open(Var, 'w') as Objeto_Escreve:
        json.dump(Nome, Objeto_Escreve)
# Foi Muito Facil, apenas Ctrl C + Ctrl V  Organizando/invertendo os blocos
'''

#10.13 vERIFICANDO SE É uSUARIO cORRETO:
import json

def Armazene_Nome():
    '''Armazena Nome De Usuário'''
    Nome_Arquivo = 'Usuario.json'
    try:
        with open(Nome_Arquivo) as Objeto:
            usuario = json.load(Objeto) #Torna ele legivel\Printavel
    except FileNotFoundError: #Caso Não exista Arquivo .JSON
        print("Arquivo Não Encontrado")
        #return None

    else: #Caso ele Exista e já tenha Algo Escrito:
        return usuario

def Novo_Usuario():
    '''Pede Por Um Novo Usuário'''
    usuario = input('Qual Seu Nome: ')
    nome_arquivo = 'usuario.json'   # Caso o primeiro Arquivo JSON não exista, Este será Criado.
    with open(nome_arquivo, 'w') as Objeto_2:
        json.dump(usuario, Objeto_2)
    return usuario

def Cumprimenta():
    '''Cumprimenta Pelo Nome'''
    usuario = Armazene_Nome()
    if usuario:
        Correto = input("É seu Nome:\t" + usuario + "\t(S/N)")
        if Correto in "Ss":
            print("Seja Bem Vindo\t" + usuario + "!")
        else:
            usuario = Novo_Usuario()
            print("Nos Lembraremos Quando Você Voltar,\t" + usuario + "!")

Cumprimenta()
