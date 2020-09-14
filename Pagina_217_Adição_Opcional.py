First_name = input('Primeiro Nome: ')
Middle_name = input('Nome Do Meio: ')
Last_name = input('Ultimo Nome: ')

def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name: #OU SE NOME DO MEIO = TRUE, EXECUTE O CODGO A BAIXO
        Full_Name = first_name + ' ' + middle_name + ' ' +last_name
    else:
        Full_Name = first_name + ' ' + last_name
    return  Full_Name.title() # É ESTA A LINHA QUE FEZ A CHAMADA (?) EU ACREDITO QUE SIM
Resultado = get_formatted_name(First_name , Last_name) #SÓ FUNCIONA COM VIRGULAS !!!!
print(Resultado)
Resultado = get_formatted_name(First_name , Last_name, Middle_name)  #Foi Necessário Mudar a Ordem Devido á Posição dos Parametros.
print(Resultado)

# Okay  It Works !!



#ASSIM, SE EU DIGITAR APENAS O PRIMEIRO E O ULTIMO NOME (SEM O DO MEIO) O PROGRAMA FUNCIONA DA MESMA FORMA
#O MIDDLE_NAME FICOU POR ULTMO, ELE ESTA COM UMA STRING VAZIA.

'''Python interpreta strings não vazias como True, portanto if middle_name
será avaliado como True se um argumento para o nome do meio estiver na
chamada da função
'''
