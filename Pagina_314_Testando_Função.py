from Func_Formata_Nome import  Formate_Nome

print('Digite Q a qualquer momento para Sair')
while True:
    First = str(input("\nDigite o Primeiro Nome: "))
    if First in 'qQ':
        break
    Ultimo = str(input("Digite o Ultimo Nome: "))
    if Ultimo in 'qQ':
        break
    Nome_Formatado = Formate_Nome(First, Ultimo)
    #print("\tNeatly formatted name: " + Nome_Formatado + ' .')
    print('\nNome Nitidamente Formatado: ' + Nome_Formatado + ' .')
