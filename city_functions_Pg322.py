#Do EXE 11.1 :
def get_formatted_name(City, Country):
    """Mostra Cidade e Pais."""
    full_name = City + ' | ' + Country
    print(full_name.upper())


#Para o Exer 11.2
def Population(City, Country, population=''):
    """Mostra Cidade e Pais."""
    full_name = City + ' ' + Country + ' ' + population
    return full_name.upper()
    #return full_name


#get_formatted_name('Minas Gerais', 'Brasil')
#Pop = Population('SP', 'Sp','2M')
#print(Pop)
