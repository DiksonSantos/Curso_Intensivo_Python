'''# remove remove todos os nomes Repetidos de Uma Lista.

pets = ['dog', 'cat', 'dog', 'golsfish','cat','rabbit','cat']
print(pets)                             #imprimiu a listo toda.

while 'cat' in pets:
    pets.remove('cat') #remove todas as ocorrencias de CAT
print(pets)             #Imprimiu com'cat' removidoSS
'''


#Pagina _199 -> Preenchendo um dicionário com dados de entrada do usuário

responses = {}   #ResponseSSS com S é a lista !
# Define uma flag para indicar que a enquete está ativa
polling_active = True

while polling_active:#Enquanto Polling For TRUE -> Pede o nome da pessoa e a resposta
    name = input('\nWhat´s Your Name? : ')
    response = input('Wich mountain would you like to climb someday? ')  #Response SEM S é a variavél\entrada de dados.
    # Armazena a Resposta No Dicionário
    responses[name] = response #Response Recebe O Conteudo Da Var NAME (Com esta linha de Comando)
    #Descobre se Outra Pessoa Vai Responder á Enquete
    repeat = input("Would you like to let another person respond? (yes/no) ") #Interessante-> Repeat é uma Var que Recebe Um INPUT
    if repeat == 'no': # Se responderem NO aqui , Isso desarma a FLAG de True Para False
        polling_active = False
    #A enquete foi concluída. Mostra os resultados
    print(('\n--- Poll Results ---'))  # Essa mensagem vai ser impressa de qualquer forma.
    for name, response in responses.items(): #Acredito que NAME se tornou Uma CHAVE e RESPONSE se Tornou Um VALOR Desta chave. Por Isso Usou o .ITEMS
        print(name + ' Would Like To Climb ' + response + '.')  #Teste com este PRINT alinhado com o IF, e Sem o metodo .ITEMS


