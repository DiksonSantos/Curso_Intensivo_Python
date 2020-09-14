#10.3 Convidados:
'''
Nome = str.title(input("Qual Seu Nome? "))
TXT = 'guest.txt'
with open(TXT, 'r+') as Objeto:
    Objeto.write(Nome)
#FUNCIONOU !!! EU FIZ SOZINHO !!!! UHUU
#___________________________________________'''

#10.4 Lista de Convidados:
'''
#Nome = str.capitalize(input('Seu Nome? '))
while True:
    Nome = str.capitalize(input('Seu Nome? '))
    print("Seja bem Vindo " + Nome)
    TXT = 'guest.txt'
    with open(TXT, 'r+') as Objeto:
        Objeto.write("\n" + Nome)
        #Tempo = Objeto.readlines()
    #for t in Tempo:
     #   print(t)
'''
'''
TXT = 'guest.txt'
print("Para Encerrar Digite Quit")

while True:
    Nome = str.capitalize(input('Seu Nome? ')) #Converte a Primeira Letra para MAIUSCULA
    if Nome in "Quit": #Maiusculo ou Minusculo Funciona
        break
    else:
        with open(TXT, 'a') as T: #Abre com Instrução de Concatenar 'a'
            T.write(Nome + '\n') #Instrução write insere no TXT o conteudo da variavel, Depois Pula uma linha.
        print("Oi " + Nome + " Você Foi Adicionado ao Livro de Visitantes") #Mensagem continua dentro do WHILE.
'''

#10.5 Enquete sobre programação:

TXT = 'guest.txt'
print("Para encerrar a Enquete Digite Exit Em NOME")
while True:
    nome = str.capitalize(input("Qual seu nome?")) #SE NÃO COLOCAR O CAPTALIZE -> NÃO FUNCIONA!
    if nome in "Exit":
        break
    else:

        Perg = str.capitalize((input("Porque Você Gosta de Programação? ")))
        with open(TXT, 'a') as TEXXXTO:
            TEXXXTO.write("Nome: " + nome + '\n')
            TEXXXTO.write("Motivo: " + Perg + '\n')
    print("Obrigado por Participar " + nome + " Seu Comentário foi Guradado")
