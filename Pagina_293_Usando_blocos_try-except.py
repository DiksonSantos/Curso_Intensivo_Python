'''
try:
    print(5/0)
except ZeroDivisionError:
    print("Não da pra Dividir por Zero")


#Se houver mais código depois do bloco try-except, o programa
#continuará executando, pois dissemos a Python como o erro deve ser
#tratado.
'''

print("Me dê Dois Numeros Para Eu dividir: ")
print("Digite 'Q' Para Sair")

'''
while True:
    Pri_Num = float(input("Digite Um Numero: "))
    if Pri_Num in "qQ":
        break
    Sec_Num = float(input("Digite Outro Numero: "))
    if Sec_Num in "Qq":
        break
        
    #Aqui Foi Colocado UM TRY, e a Linha de Baixo Foi Identada.
    Resposta = float(Pri_Num) / float(Sec_Num)
    
    #Aqui é colocado um ELSE, e a linha de baixo Identada a ele.
    print(Resposta)
'''

while True:
    Pri_Num = input("Digite Um Numero: ")
    if Pri_Num in "Qq":
        break
    Sec_Num = int(input("Digite Outro Numero: "))
    try: #Para Possibilidade de Erro de Calculo
        Resposta = float(Pri_Num) / float(Sec_Num) #Caso Ocorra Aqui
    except ZeroDivisionError: #Excessão Para Este tipo de erro...
        print("Não Da Divisão Por ZERO !") #Mostre Esta Mensagem.

    else: #Qualquer código que dependa do sucesso do bloco try é adicionado no bloco else.
        print(Resposta) #Caso Contrário, Esta.

'''
Pedimos a Python para tentar concluir a operação de divisão em um
bloco try: , que inclui apenas o código que pode causar um erro
'''
