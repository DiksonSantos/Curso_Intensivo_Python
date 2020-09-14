'''
"""Exibe Uma Saudação"""
def Greet_User(Nome):
    Nome = str(input('Qual Seu Nome? '))
    print('Hi Dearest '+Nome)

Greet_User('') #No caso Meu nome aqui é a informação com que esta função vai trabalhar

'''

#______________________________

'''A = int(input('Digite Um Numero: '))
B = float(input('Digite Um Numero: '))

def SOMA():
    C = A + B
    print(C)

SOMA()'''

#____________________________________

def greet_user(user_name): #USERNAME-> É o Parametro
    print('Hello, '+user_name.title()+' !' )


greet_user('Qualquer Coisa aqui')  #O Comando greet Imprime na tela qualquer coisa que eu Digitar Aqui (ARGUMENTO)


#_________________________
'''
def greet_user(username): #username Se Tornou Uma Variavél DENTRO da função (Ou pertencente á Função)

    print("Hello, " + username.title() + "!")
    
greet_user('jesse') #O Valor entre os parentese é dado á função para trabalha-lo
'''

'''
EXPLICAÇÃO DE COMO FUNCIONA:
A variável username na definição de greet_user() é um exemplo de
parâmetro – uma informação de que a função precisa para executar sua
tarefa. O valor 'jesse' em greet_user('jesse') é um exemplo de
argumento. Um argumento é uma informação passada para uma função em
sua chamada. Quando chamamos a função, colocamos entre parênteses o
valor com que queremos que a função trabalhe. Nesse caso, o argumento
'jesse' foi passado para a função greet_user() e o valor foi armazenado no
parâmetro username.
'''

