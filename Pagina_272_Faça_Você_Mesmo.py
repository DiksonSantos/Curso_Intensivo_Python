'''
#9.10 Importando Restaurant
#import MODULO_Classe_Restaurante_
from MODULO_Classe_Restaurante_ import *   #Só funcionou Assim :/   ???

MamaMia = Restaurant("Lanchonete", "Tapioca")
print(MamaMia.name)
print(MamaMia.cuisine_type)
'''


#9.11 -> Importando ADMIN

#from MODULO_Admin import *   #Hora Só funciona a importação seletiva Hora somente a Total...  :/ ???
from __MODULO_Admin import Admin #Eu estava importando elementos Errados. O correto é trazer ADMIN



Dikson = Admin("Dikson", "Santos", "GOW", "Dikson_@hotmail.com","SP") #Aqui Eu tinha colocado USER ao inves de ADMIN
Dikson.describe_user() #Por isto esta parte do codigo funcionava, mas haviam problemas no restante.
Dikson.greet_user()

Dikson_Privilegios = ['can reset passwords',
    'can moderate discussions',
    'can suspend accounts']

#Recessoes = ['Cant bann', "Not erase"]

'''Dikson é o nome Objeto, usando funções internas da classe Privileges.  
Creio eu que->O Objeto Dikson associado á Lista (PRIV) vazia criada antes da Função Privileges
Usa a  Classe 'Privileges para Receber\Lidar com a Lista 'Dikson_Privilegios'  '''

#Objeto(Dikson)+ LISTA DE Fora\Anterior Á Classe + Variavel_Interrna ou Atributo da Classe Que lida com Listas, +
#...Recebe Dicionario (Dikson_Privilegios)
Dikson.PRIV.Privileges = Dikson_Privilegios # Esta é a Sintaxe para inserir Listas Nesta Classe\Função.

#Se Fizer isto, ele substitui a lista anterior por esta. Nada mais:
#Dikson.PRIV.Privileges = Recessoes #Objeto + Lista_Vazia(Anterior_á_classe) + (Função\Classe a ser Usada)

print("\n O Admin " + Dikson.username + " Tem Esses Privilegios: ")
#print(Dikson.privileges)
Dikson.PRIV.show_privileges() #A lista PRIV já recebeu Dikson_Privilegios. Usa a Função SHOW_PRIVILEGES

#END


