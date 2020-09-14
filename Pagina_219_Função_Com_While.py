def nome_formatado(primeiro_nome, ultimo_nome): #Primeiro Parametro Segundo Parametro
    Nome_Inteiro = primeiro_nome + ' '+ ultimo_nome #É o que esta função Faz
    return  Nome_Inteiro.title()  # Acredito que isso possibilita exportar o que a função faz para fora dela
#Este é um Loop Infinito !
while True:
    print('\nPor Favor me diga Seu Nome: ') #Tudo isso a baixo esta dentro do WHILE, ou seja esta sendo usado graças ao RETURN
    print("(Digite 'Quit' a Qualquer Hora Para Encerrar.)")
    Nome_1 = input('Primeiro Nome: ')
    if Nome_1 in 'QUIT quit Quit': #Fiz segundo Guanabara ensinou no video 56
        break # Se a condição a cima for real, ele para o procedimento ou da Stop no WHILE
    Last_Name = input('Ultimo Nome: ')
    if Last_Name in 'QUIT quit Quit':
        break

    N_formatado = nome_formatado(Nome_1,Last_Name) #É uma variavél para receber a função, e com esta variavel poderemos trabalhar
    # A cima => a Variavel N_forma.. recebe a função nome_format... para trabalhar com os Inputs Nome_ & Last_name...
    print('\nHello '+N_formatado+'!') # Como aqui

