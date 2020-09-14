Nome_1 = str(input('Nome: '))
Nome_2 = str(input('Sobrenome: '))
try:
    Age = int(input('Quantos Anos?: '))
except:
    pass
def build_person(first_name, last_name):
    '''Devolve Um Dicionario Com informações sobre Uma Pessoa'''

    person = {'First': first_name, 'Last': last_name}
    try:
        if Age:
            person['Idade'] = Age #Ou -> O dicionario PERSON recebe a chave idade com o valor inserido em AGE
        return  person #Esta na mesma linha do IF Ou-> Se algo for inserido em AGE Retorne O Dicionario Person.
    except:
        print("Tente Novamente, e Digite Idade")
musician = build_person(Nome_1, Nome_2) #Aqui os argumentos Relacionados Aos Parametros. MUSICIANS Recebeu a Função na totalidade.
print(musician)

'''
Ele armazenou o Nome_1 na Chave first do Dicionario, e o Nome_2 , na chave last_name
retornou o Dicionario\person 
MUSICIAN É = Á Função\DEF com os Argumentos que são Os INPUTs
'''

# Continuar Em Pag 219 ->  Usando uma função com um laço while
