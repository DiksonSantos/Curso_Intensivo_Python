class Car():
    def __init__(self, make, model, year):
        """Inicializa os atributos que descrevem um carro."""
        self.make = make # Este MAKE depois do = é o mesmo dos Parametros a cima.
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Devolve um nome descritivo, formatado de modo elegante."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        #Mostrar_Grande = long_name.upper()
        #return long_name.upper()
        #return Mostrar_Grande #Funciona Com Return TAMBÉM, mas olhe na linha 39 como seria necessário usar.
        print(long_name.upper())

    def read_odometer(self):
        """Exibe uma frase que mostra a milhagem do carro."""
        print("Este Carro Tem " + str(self.odometer_reading) + " Milhas Rodadas.")

    def update_odometer(self, mileage):  #Da pagina 252
        """
Define o valor de leitura do hodômetro com o valor especificado
Rejeita a alteração se for tentativa de definir um valor menor
para o hodômetro
"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
            print("Nova Kilometragem ", mileage) #Caso o Valor de entrada em Update_Odometer seja maior do que o em Odometer_Reading, ele Mostra esta mensagem.
        else:
            print("Você Não pode retroceder o Odometro")


my_new_car = Car('audi', 'a4', 2016)
#print(my_new_car.get_descriptive_name())
my_new_car.get_descriptive_name()

my_new_car.odometer_reading = 22  #Com ou sem este bloco funciona -> O valor é atualizado P/ 23
my_new_car.read_odometer()

Val_Odometro = int(input("Valor Do Odometro: ")) # Esta linha eu incrementei P facilitar a compreenção do codigo.

my_new_car.update_odometer(Val_Odometro)  #Da Pagina 252 -> Referente ao UPDATE_ODOMETER(Argumento = 23)
#Agora com as novas intruções IF ELSE -> Se o Valor da linha de cima aqui no caso 20 for menor que o valor original (22), ele mostra a Mensagem do ELSE:
my_new_car.read_odometer() #Como a função Read_Odometer recebeu o valor de Update_Odometer que é 23, ela vai mostra-lo aqui por ultimo



#Continuar na pagina 253 Oficial
# http://pythonclub.com.br/introducao-classes-metodos-python-basico.html
