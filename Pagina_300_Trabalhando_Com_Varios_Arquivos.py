

def contador_Palavras(Nome): #Aqui tem que ter Um PARAMETRO, OU o nome da Variavel que Guarda o TXT ou o caminho do mesmo.
    try:
        with open(Nome) as Objeto:
            conteudo = Objeto.read()
    except FileNotFoundError: #Caso dê Pau, ou ele não ache o Arquivo: Mostra a mensagem a baixo:
        msg = 'Arquivo Não Encontrado, Desculpe ;/' #SE SUBSTITUIR ESTA LINHA E A DE BAIXO PELA PALAVRA RESERVADA 'PASS'
        print(msg) #..O CODIGO SIMPLESMENTE CONTINUA SEM DIZER NADA.
    else:# ... Se tudo funcionar Beleza, ele continua..  :
        #Conta o Numero aprox de PALAVRAS  do arquivo
        #Método split() para obter uma lista de todas as palavras do livro (Acredito que Palavras ao Inves de Letras).
        Palavras = conteudo.split()  # Split serve para Dividir Strings _> acredito q ele não vai VER linhas e sim Palavras com Este metodo.
        Num_Palavras = len(Palavras)  #contando as divisões da String
        print("O Arquivo " + Nome + 'Tem Mais Ou Menos: ' + str(Num_Palavras) + " Palavras")

#Nome_Arq = 'Alice in Wonderland.txt'  #Nome da VAR que Guarda ...

#contador_Palavras(Nome_Arq)

#
#Se colocar um TXT inexistente por ultimo é Pior Ainda, ai ele nâo mostra Numero NEHUM
Arquivos = ['Não Existe.txt',  'programming.txt',  'Tst_Read__.txt']
for X in Arquivos:
    print(X)
    contador_Palavras(X) #Aqui precisa estar Identado para Mostrar TODOS os TXTs da Variavel 'Arquivos'

#Copiei o Codigo da Apostila->(Mesma coisa) NÃO MOSTRA RESULTADO IGUAL AO MOSTRADO NA APOSTILA !
#..Mostra somente o numero de Palavras do Ultimo texto apresentado na Lista (Neste caso: 'Arquivos'
''''
Eu estava colocando na linha 3 ao inves de 'Nome' , colocava o 'Nome_Arq' que é
a Variavel que recebe o TXT ou o caminho P/ o mesmo. 
MAS-> Para não ter que ficar alterando la toda hora que quiser ler um TXT diferente
eu coloquei apenas 'Nome' que é Generico. Assim a unica coisa de que precisamos é
Inserir em 'contador_Palavras('VAR')'  o Nome da variavel que guarda o TXT, e não mais
 necessario alterar outros trechos do Codigo.   
'''

