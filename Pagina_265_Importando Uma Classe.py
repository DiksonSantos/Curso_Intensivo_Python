
#from __Modulo_CAR import Car, ElectricCar #Aqui estou importando 2 Tipos de Carro
from __Modulo_CAR import *  # Aqui tem tudo incluindo baterias eletricas ...

Carro = Car("audi", "a3" ,1997)
print(Carro.get_descriptive_name())
Carro.Gasolina_Tk_Cheio()

print("\n")

Eletrico = ElectricCar("Tesla", "X2", 2017)
print(Eletrico.get_descriptive_name())
Eletrico.descrever_BATERIA()
print(Eletrico.Nivel_Bateria)
Eletrico.Gasolina_Tk_Cheio()


'''
Aqui ele pede para tirar trechos do EXE 9.9 para criar modulos. 
Não precisa, eu entendi a logica, Sei como criar os modulos... 

@Importando várias classes de um módulo:
from car import Car, ElectricCar@
Exatamente como ja foi visto antes. Só que ao inves de DEFs estamos 
Importando CLASSES (Class)

Ex:
my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
'''

