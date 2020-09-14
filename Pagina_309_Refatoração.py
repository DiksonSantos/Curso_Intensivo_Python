import json

def Cumprimenta_Usuario():
    """Saúda o usuário pelo nome."""
    nome_arquivo = '309.json' #O JSON.DUMP-> CRIA este arquivo .JSON
    try:
        with open(nome_arquivo) as Objeto_F: #Se esse arquivo existir
            Nome_Usuario = json.load(Objeto_F) #lemos o nome do usuário de volta para a memoria. Load->Surrupia p/ Nome_Usu...

    #O Bloco a baixo só é executado Caso o .JSON com o nome esperado Não esteja lá.
    #Mas se não existir arquivo nenhum da pau.
    except FileNotFoundError: # Se o Arquivo Criado\Rodado anteriormente não estiver lá -> O Codigo a baixo é Rodado.
        Nome_Usuario = input('Nome: ') #-> É inserida informação na variavél
        with open(nome_arquivo, 'w+') as Objeto_F: # Na Linha de baixo o conteudo do INPUT é acrescentado ao Objeto
            #... que é aberto aqui como Objeto_F
            json.dump(Nome_Usuario, Objeto_F) #Então usamos json.dump() para armazenar o INPUT  no Objeto_F
            print('Nós Vamos Te Lembrar Quando Você Voltar, ' + Nome_Usuario) #Exibe conteudo inserido no arquivo .JASON
    else: #Quando o Arquivo.JSON já EXISTE o bloco a baixo Roda:
        print("Bem Vindo De volta: " + Nome_Usuario) #Se O Arquivo ('username.json') Já Existir Ou Se já Estiver Escrito, Ele Printa Isso
#...ou seja, Ele já vai direto no objeto sem Executar o Bloco EXCEPT, e mostra o conteudo que já foi colocado no .JSON

Cumprimenta_Usuario()
