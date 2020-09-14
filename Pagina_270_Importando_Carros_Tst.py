from __Modulo_Tudo_Eletrico import ElectricCar
from __Modulo_CAR import Car, Batery

Carro = Car("Ford", "Ka", 2005)
print(Carro.get_descriptive_name())
Carro.increment_odometer(100) # Valor deste atributo no inicio do codigo Car era 0, Foi incrementado com 100
Carro.Gasolina_Tk_Cheio()
Carro.read_odometer() # Aqui ele mostra o novo valor Incrementado.

print("\n")

Eletrico = ElectricCar("Tesla", "M-2", 2018) #Instanciado
print(Eletrico.get_descriptive_name()) #Da classe Car
Eletrico.descrever_BATERIA() #Da classe EletricCar
Eletrico.Bateria_.upgrade_battery() # Da classe Batery


"""
O que a apostila quis explicar é que é possivel e também uma boa ideia importar um modulo dentro de 
outro modulo se preciso for.

Este arquivo aqui Não é um Modulo, mas poderia ser. 
Virou 'Baguncics' o que a apostila estava pedindo, assim decidi improvisar.
"""
