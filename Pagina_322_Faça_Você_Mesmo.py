#11.1 Cidade, País:
#Metodo_01
#import city_functions_Pg322
from city_functions_Pg322 import get_formatted_name, Population
get_formatted_name('São Paulo', 'Brasil')

#Metodo_2:
#from city_functions_Pg322 import get_formatted_name
#get_formatted_name('São Paulo', 'Brasil')
#__________________________________________________
'''
11.1 Concluido no Arquivo 'test_cities_PG322_.py'
'''

#11.2 População
Pop = Population('Campinas,', 'Brasil,', 'População: UM Milhão~') #Ok: Funciona com ou Sem o Ultimo Parametro.
print(Pop)

