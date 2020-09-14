
'''

#PRIMEIRA FORMA DE ABRIR UM .TXT  #Eu acredito que esta sintaxe é o Python 2
arq = open('pi_digits.txt', 'r')
#arq.read()
print(arq.read().rstrip())
arq.close()



#FORMA DA APOSTILA P/ ABRIR UM .TXT  #Aparentemente Uma sintaxe Moderna.
with open('pi_digits.txt') as file_object: #O Argumento da Função OPEN é o arquivo que queremos abrir + Cria um Alias
    contents = file_object.read() #...Alias chamado file_object com a função READ (usando . como nas funções DEF
    print(contents.rstrip()) #...que é guardado em 'contents' e Printado Aqui
    #RSTRIP remove a ultima linha em branco gerada quando o TXT é mostrado. MAS aqui não notei diferença alguma na saida.
#O arquivo TXT deve estar na mesma pasta dos arquivos .PY que abre os TXT



#Na Primeira maneira de abrir, no final tem Close, na segunda já não tem, pois o WITH fecha o arquivo depois que
#não for mais
#necessário acessá-lo.



#Abrindo arquivo em Local Especifivco:
Caminho_path = 'C:/Users\Dikson\PycharmProjects\Curso_Intensivo_De_Python_Livro_Eric_Mat\Todos Exercicios_Resolvidos !!.txt'
with open(Caminho_path) as file_object:
        print(file_object.read())

'''
#Resumindo isso aqui serve para mostrar o texto com espaço entre as Linhas.

#armazem = 'C:/Users\Dikson\PycharmProjects\Curso_Intensivo_De_Python_Livro_Eric_Mat\Tst_Read__.txt'
armazem = '/home/dikson01/PycharmProjects/Data Analisis 30 AUlas.txt'
with open(armazem) as objeto: #Objeto, pode ser qq palavra aqui...
        linhas = objeto.readlines() #Aqui Usei o Metodo .readlines()
for linha in linhas:
        print(linha)  # .rstrip()  -> Novamente Retira os Espaços em Branco

'''
#Obtive o mesmo efeito com o seguinte codigo:
armazem = 'C:/Users\Dikson\PycharmProjects\Curso_Intensivo_De_Python_Livro_Eric_Mat\Tst_Read__.txt'
with open(armazem) as objeto: #Objeto, pode ser qq palavra aqui...
    for linha in objeto: #Aqui a linha de baixo NÃO tem o metodo .readlines() ,mas estranhamente tem os mesmos resultados
        print(linha)  # .rstrip()  -> Novamente Retira os Espaços em Branco
#Resumindo -> Ele também coloca um espaço entre as linhas.
'''

'''
1-Apontar o local do arquivo\Texto Para guarda-lo numa Variavel
2-Usar o metodo OPEN(+) para abrir o conteudo da variavel. E Converter isto para Um Objeto. (Usando um Alias).
3-Cria outra variavel (LINES) Para Receber este Objeto Convertido, e Usar o metodo READLINES() Neste Objeto.
4- USA UM LAÇO FOR para percorrer o conteudo da Variavel que guarda o Objeto (Como se fosse uma lista), lendo cada linha
como se fossem itens de uma lista (eu creio).
5- Printa as linhas separadamente graças ao metodo READLINES.
'''
