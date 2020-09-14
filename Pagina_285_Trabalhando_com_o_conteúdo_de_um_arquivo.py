'''
Começamos abrindo o arquivo e armazenando cada linha de dígitos em
uma lista
'''
armazem = 'C:/Users\Dikson\PycharmProjects\Curso_Intensivo_De_Python_Livro_Eric_Mat\Tst_Read__.txt'
with open(armazem) as Arquivo_Objeto:
    linhas = Arquivo_Objeto.readlines()

'''
String__ é uma variável
 para armazenar os dígitos do texto aberto.
'''
String__ = ''


for linha in linhas: #O Laço FOR percorre o arquivo -> LINHAS  Recebeu o TXT Convertido em Objeto.

    #Usando o RSTRIP nos livramos dos espaços entre as palavras, para sabermos com exatidão a quant de letras (684)
    String__ += linha.rstrip() #Aqui a variavel Vazia Recebe as linhas (tidas como Itens de Uma Lista)
print(String__) #Imprime Conteudo Recebido.

'''Neste caso o Numero 684 que aparece por ultimo É referente ao tamanho ou quant de caracteres do texto 
convertido em uma string'''
print(len(String__))

'''
Quando Python lê um arquivo-texto, todo o texto do arquivo é interpretado
como uma string. Se você ler um número e quiser trabalhar com esse valor em
um contexto numérico, será necessário convertê-lo em um inteiro usando a
função int() ou convertê-lo em um número de ponto flutuante com a função
float().
'''
#Continua no final da Pag 286 , Inicio da 287. (De 552)
