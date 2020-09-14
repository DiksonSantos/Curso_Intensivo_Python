Nome = str(input('Digite Seu Prmeiro Nome: '))
Sobrenome = str(input('Digite Seu Sobrenome: '))

def get_formatted_name(First_Name, Last_Name):
    '''Devolve Um Nome Formatado de Forma Elegante'''
    full_name = First_Name +'  '+Last_Name #Criou Uma Variavel Dentro Da Função Para Receber os Dois Parametros desta.
    return  full_name.title()  #Pelo que percebi a função RETURN é para exportar FULL_NAME de dentro para fora da Função.
Musico = get_formatted_name(Nome,Sobrenome) # Variavel que armazena o Valor de Retorno (Musico)
print(Musico)
