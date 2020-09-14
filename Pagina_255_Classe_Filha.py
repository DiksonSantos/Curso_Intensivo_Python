class Car():
    """Uma tentativa simples de representar um carro."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles onit.")


    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")


    def increment_odometer(self, miles):
        self.odometer_reading += miles


#Trecho Novo a Partir Daqui:

class EletricCar(Car):
    '''Novo Veiculo Eletrico, ou Classe filha da Classe CAR'''

    def __init__(self, make, model, year):
        '''Repetindo OU Inicializando Atributos da classe PAI'''
        super().__init__(make, model, year) #MAKE MODEL YEAR tem que ser Identicos aos da classe anterior. __init__() ->Chama o init da classe PAI
'''
A função super() em x é uma função especial que ajuda Python a criar
conexões entre a classe-pai e a classe-filha. Essa linha diz a Python para
chamar o método __init__() da classe-pai de ElectricCar, que confere
todos os atributos da classe-pai a ElectricCar. O nome super é derivado de
uma convenção segundo a qual a classe-pai se chama superclasse e a classefilha
é a subclasse.
'''
Meu_Tesla = EletricCar("Tesla", "Modelo-S", 2018)
print(Meu_Tesla.get_descriptive_name())

Meu_Tesla.update_odometer(800)
Meu_Tesla.increment_odometer(80) # (Acredito que) Conforme a sequencia do codigo, esta função Increment, só pode ser chamada depois da UPDATE
print(Meu_Tesla.read_odometer())

