class Car():
    """Uma tentativa simples de representar um carro."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title() #Nem precisou do PRINT Usando o Return

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")


    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")


    def increment_odometer(self, miles):
        self.odometer_reading += miles

class ElectricCar(Car):
    """Representa aspectos específicos de veículos elétricos."""
    def __init__(self, make, model, year):
        """Inicializa os atributos da classe pai.
        Em seguida, inicializa os atributos específicos de um carro elétrico"""
        super().__init__(make, model, year) #Herdados
        self.Nivel_Bateria = 70  #Atrib Exclusivo

    def descrever_BATERIA(self):
        '''Capacidade da Batera'''
        print("This Car has a " + str(self.Nivel_Bateria) + "-kWhbattery")

#"This Car has a " + str(self.Nivel_Bateria()) + "KWh"
Meu_Tesla = ElectricCar("Tesla", "Model-S", 2016)
print(Meu_Tesla.get_descriptive_name())
Meu_Tesla.descrever_BATERIA()

Carro_Pilha = ElectricCar("Raiovac", "Alcalino", 2019)
print("\n"+Carro_Pilha.get_descriptive_name())
Carro_Pilha.Nivel_Bateria = 90  #Fui eu quem fiz esta Linha :0
Carro_Pilha.descrever_BATERIA()

print("\n")

Fumaça = Car("Ford","S-10",1986)
print(Fumaça.get_descriptive_name())
Fumaça.increment_odometer(10)
Fumaça.read_odometer()

# Continuar em ->   Sobrescrevendo métodos da classe-pai Pag 259
