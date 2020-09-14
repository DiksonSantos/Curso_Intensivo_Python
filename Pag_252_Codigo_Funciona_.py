#Cod Até a Pag 252:

class Car():
    def __init__(self, make, model, year):
        """Inicializa os atributos que descrevem um carro."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):

        """Devolve um nome descritivo, formatado de modo elegante."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Exibe uma frase que mostra a milhagem do carro."""
        print("This car has " + str(self.odometer_reading) + " miles onit.")

    def update_odometer(self, mileage):  #Da pagina 252
        """Define o valor de leitura do hodômetro com o valorespecificado."""
        self.odometer_reading = mileage #Ou: A função de cime, recebe o resultado desta aqui


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

#my_new_car.odometer_reading = 22  #Com ou sem este bloco funciona -> O valor é atualizado P/ 23
#my_new_car.read_odometer()

my_new_car.update_odometer(23)  #Da Pagina 252 -> Referente ao UPDATE_ODOMETER(Argumento = 23)
my_new_car.read_odometer() #Como a função Read_Odometer recebeu o valor de Update_Odometer que é 23, ela vai mostra-lo aqui por ultimo
