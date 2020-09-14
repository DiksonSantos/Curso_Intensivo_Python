'''
#10.6 Adição:
class Calculator():
    def __init__(self,N, N_):

        self.Num = N
        self.Num_ = N_
        Res = N + N_
        print("Soma ", Res)


    def Multip(self, N, N_1):

        Num = N
        Num__=N_1
        Prod = Num * Num__
        print("Multiplicação: ", Prod)


#try:
    #num_1 = int(input("Numero "))
    #num_2 = int(input("Outro Numero "))


    #show_nums(Somar(num_1, num_2))

#except ValueError:
#    print("Digite Numeros, Não Letras ;)")
try:
    num_1 = int(input("Numero "))
    num_2 = int(input("Outro Numero "))


    Maquina = Calculator(num_1,num_2)
    Maquina.Multip(num_1,num_2)
except:
    print("Digite Numeros, Não Letras ;)")
#Maquina.show_nums(Calculator(num_1,num_2))
#We Did It!
'''

'''
def Somar(N, N_):
    #Func Somar
    Num = N
    Num_ = N_
    Res = N + N_
    return Res



def show_nums(El):
    #Função Mostrar
    print(El)


try:
    num_1 = int(input("Numero "))
    num_2 = int(input("Outro Numero "))
    
    show_nums(Somar(num_1, num_2))
    
except ValueError:
    print("Digite Numeros, Não Letras ;)")


'''


'''
#10.7 Calculadora com while:
print("Tecle -1 Para Sair")
while True:
    class Calculator():
        def __init__(self,N, N_):
            #Func Somar 
            self.Num = N
            self.Num_ = N_
            Res = N + N_
            print("Soma ", Res)


        def Multip(self, N, N_1):
            #Função Multiplicar
            Num = N
            Num__=N_1
            Prod = Num * Num__
            print("Multiplicação: ", Prod)


    try:
        num_1 = int(input("Numero "))
        if num_1  == -1:
          break

        num_2 = int(input("Outro Numero "))
        if num_2  == -1:
          break



        Maquina = Calculator(num_1,num_2)
        Maquina.Multip(num_1,num_2)
    except:
        print("Digite Numeros, Não Letras ;)")
#Ok We did it!
'''
'''
#10.8 - Gatos e Cachorros:
with open('cats.txt', 'r+') as TExxto:
    TExxto.write('Xano, Nino, Mustafá \n') #Aceita UMA String só por Parenteses.
    TExxto.write('Zeus, Sujinho, Fubá')
    TExxto.write('\nSpot')
with open('cats.txt') as TXT:  #Engraçado: Não precisou por 'r' ou 'r+'
    print(TXT.read())

print('\n')

with open('dogs.txt', 'r+') as DOG:
    DOG.write('Jambo, Stanheg\n')
    DOG.write("Pitoco, Jipe")
    DOG.write('\nNorman Mayler, Mylow, Spok')
with open('dogs.txt', 'r') as Sobaka:
    print(Sobaka.read())
#Ok We Did It!
'''
'''
#10.9 Gatos e Cachorros silenciosos:
TXTs = ['dogs.txt', 'cats.txt']

for TX in TXTs: #Percorre Itens\Textos da Lista
    print('Lendo Arquivo: ' + TX) #Pega estes Itens e Usa 'With Open'
    #print("\n")
    try: #Ação natural:
        with open( TX ) as T:
            Armazem = T.read()
            print(Armazem + '\n')
    except FileNotFoundError: #Caso Não encontre o Arquivo.
        print("Desculpe, Arquivo Não Encontrado  :/")
'''

#10.10 Palavras comuns:
Palavra = str.upper(input("Digite a palavra que quer Buscar: "))
with open('Segunda_Guerra.txt', 'r+') as Objeto:
    Armazem = Objeto.read()
    Objeto.write('WW2 History++')
    #for Arm in Armazem:
    print(Armazem)
    #Se vc usa o .LOWER tem que escrever no Count Tudo em Minuscula pra ele encontrar a palavra em qualquer tamanho;
    print('Apareceu', Armazem.upper().count(Palavra), 'Veze(s) no exto' )

#Continua na Pag 305
