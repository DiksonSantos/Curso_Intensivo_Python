'''
Titulo = 'Alice in Wonderland'
Tit = Titulo.split()

print(Tit)
'''

Nome_Arq = 'Alice in Wonderland.txt'   #Aponta Caminho
try:  #Caso dê Pau de Não encontrar, pois é isso que o bloco segunte faz: Encontrar e Abrir
    with open(Nome_Arq) as Alice_Obj:   #Abre o TXT e converte P/ Objeto.
        conteudo = Alice_Obj.read()   #Objeto é convertido dentro da Var; para ser lido
except FileNotFoundError: #Caso não encontre -> Mostre a mensagem a baixo:
    msg = "Desculpe '" + Nome_Arq + "'Não Existe"
    print(msg)
else: #Caso dê tudo certo:
    #Conta o Numero aprox de palavras no Arquivo de Texto.
    Palavras = conteudo.split() # -> Tirar os espaços entre as Palavras
    Num_Palavras = len(Palavras) #Agora conta quantas letras tem (sem os Espaços)
    #Mostra o nome do Arquivo + Converte o Numero de palavras Para STRING
    print("O Arquivo " + Nome_Arq + "' \nTem Aproximadamente: " + str(Num_Palavras) + "Palavras")


#Continua Na Pag 300 (Finalmente).
