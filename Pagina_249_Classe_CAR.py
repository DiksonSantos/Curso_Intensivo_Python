"""
O que faz o 'self.variavel' dentro de uma função?
-> Torna esta variavel interna acessivel ao Objeto caso seja necessário, Ex;

A = Car.read_odometer.odometer_reading    -> a Variavel interna odometer_reading ficou acessivel ao Objeto A.
"""

class Car():

    def __init__(self, fabrica, modelo, ano):
        self.make =  fabrica
        self.model = modelo
        self.year = ano
        self.odometro_leitor = 0

    def obtenha_description_nome(self):
        #print("Fabricas: " + self.make)
        #print("Modelo: " + self.model)
        #print("Ano de Fabricação " + str(self.year))
        long_name = self.make + " " + self.model + " " + str(self.year)
        return long_name.upper()

    def read_odometer(self):
        """Exibe uma frase que mostra a milhagem do carro."""
        print("This Car Has " + str(self.odometro_leitor) + " Miles on It")


    def update_odometer(self, mileage):
        """Define o valor de leitura do hodômetro com o valorespecificado."""
        self.odometer_reading = mileage


Meu_novo_Carro = Car("Wolks ", "BMW ", 2018) #Aqui é passado as informações/parametros (como se fosse la pra primeira linha)
print(Meu_novo_Carro.obtenha_description_nome()) #Fabrica e Modelo (somente)

Meu_novo_Carro.update_odometer = 25 #Aqui para o Bloco Ler_Odometro não mostrar 0 , passamos o valor 25 para ser mostrado
'''A maneira mais simples de modificar o valor de um atributo é acessá-lo
diretamente por meio de uma instância.'''
Meu_novo_Carro.read_odometer() #Aqui ele esta chamando o Bloco Ler_Odometro


Meu_novo_Carro.update_odometer(23)
Meu_novo_Carro.read_odometer()




#O Codigo a cima esta todo lazarentiado

'''
#A baixo esta o trecho Original da apostila

class Car():
    def __init__(self, make, model, year):
        """Inicializa os atributos que descrevem um carro."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        
        print("Fabricas: " + self.make)
        print("Modelo: " + self.model)
    def read_odometer(self):
        """Exibe uma frase que mostra a milhagem do carro."""
        print("This car has " + str(self.odometer_reading) + " miles onit.")
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
'''
