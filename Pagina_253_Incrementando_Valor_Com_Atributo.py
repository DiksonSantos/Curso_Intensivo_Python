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
        return long_name.title()

    def read_odometer(self): # Este Bloco (Acredito eu) Serve simplesmente p\ mostrar o valor Defalt do inicio
        """Exibe uma frase que mostra a milhagem do carro."""
        print("Este Carro Tem " + str(self.odometer_reading) + " Milhas Rodadas.")

    def update_odometer(self, mileage):  #Da pagina 252
        """
Define o valor de leitura do hodômetro com o valor especificado
Rejeita a alteração se for tentativa de definir um valor menor
para o hodômetro
"""

        if mileage >= self.odometer_reading: #Se o valor inserido em UPDATE_ODOMETER for maior que 0, este valor sera inserido no valor Defalt
            self.odometer_reading = mileage #Ou -> Inicializa odometer_reading para receber o valor de mileage
            print("Nova Kilometragem ", mileage) #Caso o Valor de entrada em Update_Odometer seja maior do que o em Odometer_Reading, ele Mostra esta mensagem.
        else:
            print("Você Não pode retroceder o Odometro")
            #Se não for maior -> Não ha linha aqui indicando = Ou Recebe, e ele ainda mostra esta mensagem (simples).


#A Unica diferença deste codigo para o codigo da Pag_252\253 é que apaguei a parte de maixo deles e substitui por esta.

    def increment_odometer(self, miles):
        '''Soma a Quantidade Especificada ao Valor de Leitura do Hodometro'''
        self.odometer_reading += miles

Carro_Japa = int(input("Subaru KMs: ")) #Esta Linha eu Adicionei Pra ver

my_used_car = Car('subaru', 'outback', 2013) #My_Used_Car é uma  INSTANCIA da CLASSE CAR
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(Carro_Japa) # Esta função Soma este valor  ao Update Odometer (Penso EU).
my_used_car.read_odometer()



print("\n"+"\n")
#A Parte de baixo é o Codigo da Pag 252 sendo re adicionado aqui:

Val_Odometro = int(input("Valor Do Odometro_: ")) # Esta linha eu incrementei P facilitar a compreenção do codigo.

my_new_car = Car('audi', 'a4', 2016)  #Esta é uma Outra Instancia da classe Car
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(100)  #Soma á Odometer_Reading (Que éra 0, e adiciona este 100)
my_new_car.read_odometer() #Acho que na verdade deveria se chamar Printa Odometro.
my_new_car.increment_odometer(Val_Odometro)
#my_new_car.odometer_reading = 22  #Com ou sem este bloco funciona -> O valor é atualizado P/ 23
my_new_car.read_odometer() #Tem Duas Linhas Desta



'''
#Agora com as novas intruções IF ELSE -> Se o Valor da linha de cima aqui no caso 20 for menor que o valor original (22), ele mostra a Mensagem do ELSE:
my_new_car.read_odometer() #Como a função Read_Odometer recebeu o valor de Update_Odometer que é 23, ela vai mostra-lo aqui por ultimo
my_new_car.increment_odometer(Val_Odometro)
'''
