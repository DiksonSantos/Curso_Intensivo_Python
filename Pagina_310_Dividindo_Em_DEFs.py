import json


#Essa função de Armazenar é Uma Piada...
def Armazenar_nome_usu():
    criar_arquivo_JSON = 'Arquivo_P_310+_.json' #Poderia Estar Vazia ou com '' Que ia funcionar do mesmo Jeito.
    try: #Faça Isso:
        with open(criar_arquivo_JSON) as Objeto_N:
            User_Name = json.load(Objeto_N) #LOAD: TORNA LEGIVEL ou 'PRINTAVEL'
    except FileNotFoundError: #Caso NÃO haja NENHUM Arquivo, o Bloco a Baixo Roda:
        return None #Ou - > Retorne NADA
    else:
        return User_Name #Caso contrario, ou Se -> Houver já algum arquivo, retorne o que estiver carregado em User_Name

def Cumprimenta():
    'Cumprimenta Users'
    #Uma vez que pela ordem a função a cima já rodou e criou o JSON:
    Nome_Usuario = Armazenar_nome_usu() #Aqui Ele Chama a Função de Cima que é feita Para CRIAR UM ARQUIVO.JASON
    if Nome_Usuario: #Ou Se Nome_Usuario Existir:
        print("Bem Vindo De Volta\t" + Nome_Usuario + '!') #Quando o Arquivo-> Arquivo_P_310_.json Já Existe, Esse Print é Exibido.
    else: #Daqui p/Baixo ele Cria um Arquivo.JSON , Se ele não Existir Para ser CUMPRIMENTADO (Caso Ñ tenha NADA em Nome_Usu:
        Nome_Usuario = input("Digite Um Nome Para Usuario: ") #Pede Um nome
        Nome_ARQUIVO = 'Usu_EX_PG-310.json' #Cria Um Arquivo.JSON P/ por o Nome_Usuario.
        with open(Nome_ARQUIVO, 'a+') as Objeto_S : #Transforma o Arquivo JSON num Objeto
            json.dump(Nome_Usuario, Objeto_S) #Transfere o Nome_Usu.. Para o Objeto (que é o Arquivo JSON)
            print("Bem Vindo !\t" + Nome_Usuario + '_') #Esse PRINT É mostrado Quando o Usu_EX_PG-310.json É Criado
            #... Ou Quando o *Arquivo_P_310_.json* NÃO Existir.

#Armazenar_nome_usu() #Não voga NADA chamar esta Função Aqui.
Cumprimenta()  # Acredito que -> Por esta função Usar a de cima, chamando Esta é o mesmo Que Chamar as DUAS

'''
Toda vez ele Vai escrever Bem Vindo, Pois Ele Usa a Função de Cima a Qual CRIA um Arquivo JSON.
A Função de Baixo, só Renomeia ele para 'Usu_EX_PG-310.json' , e Diz BEM VINDO DE VOLTA. 

Acumula Nomes Graças ao 'a+'.
'''

#CONTINUA NO INICIA DA PAG 311
