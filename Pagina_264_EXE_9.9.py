# 9.9 Upgrade Bateria:

class Car():
    """Uma tentativa simples de representar um carro."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.tanque = 80

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

    def Gasolina_Tk_Cheio(self):
        print("Quantidade no tanque de combustivél é:{} ".format(self.tanque)+"Litros")

class Batery():
    '''Modelando Uma Bateria Para Um Carro Eletrico'''
    def __init__(self,Nivel_Bateria=95): #Aqui só se aceitava os valores 80 e 95 para o codigo funcionar. Eu melhorei o Codigo
        '''Inicializando Caracteristicas\Atrib da Bateria'''
        self.Volume_Bateria = Nivel_Bateria

    def Descreve_Bateria(self):
        '''Frase P/ Descrever Nivel da Batera'''
        print("A Bateria deste Carro Tem: " + str(self.Volume_Bateria) + "KWh")

    def get_range(self):
        '''Exibe Distancia Capaz de Percorrer'''
        if self.Volume_Bateria <= 80:  #Com >=  <= Posso colocar Qualquer Valor em Nivel_Bateria
            range = 240
        elif self.Volume_Bateria >= 95:
            range = 270

        message = "Autonomia Aproximada = " + str(range) #+ "Milhas Com a Bateria Cheia"
        message += " Milhas Com a Bateria Cheia" #message recebe message + "String á frente"
        print(message) #mostra mensagem concatenada

#Minha Solução:
    def upgrade_battery(self, New_Size=98):
        if New_Size > self.Volume_Bateria: #Alterei de '!=' para '>' em 02-02-2019 - Funciona TBM !
            self.Volume_Bateria = New_Size #Atributos de fora desta função devem Ser Inicializados com Self
            #Fim = New_Size
            print("Nova Carga De Bateria = ", New_Size)
    '''
#Solução do Autor:
    def upgrade_battery(self):
        """Upgrade the battery if possible."""
        if self.battery_size == 60:
            self.battery_size = 85
            print("Upgraded the battery to 85 kWh.")
        else:
            print("The battery is already upgraded.")

'''
class ElectricCar(Car):
    """Representa aspectos específicos de veículos elétricos."""
    def __init__(self, make, model, year):
        """Inicializa os atributos da classe pai.
        Em seguida, inicializa os atributos específicos de um carro elétrico"""
        super().__init__(make, model, year) #Herdados
        self.Bateria_ = Batery() #Este Atrib recebe a Class Batery (Que esta com o Valor Defalt de 80)
        self.Nivel_Bateria = 70  #Atrib Exclusivos de carro eletrico.

    def descrever_BATERIA(self):
        '''Cap da Batera -METODO SOBRE-ESCRITO-'''
        print("This Car has a " + str(self.Nivel_Bateria) + " :kWhbattery")

    def Gasolina_Tk_Cheio(self):  #REPETINDO O METODO AQUI, ELE SOBREESCREVE O ANTERIOR
        print("Este carro é Eletrico Dhãaarr")
'''
Meu_Tesla = ElectricCar("Tesla", "M2", 2018)
Meu_Tesla.descrever_BATERIA()
Meu_Tesla.get_descriptive_name()'''

Carro =ElectricCar("Fabricante", "Modelo", 1999)
print(Carro.get_descriptive_name())
print("Primeiro Nivel Da Batera: ", Carro.Nivel_Bateria)
#Carro.Nivel_Bateria = ""
#Carro.get_descriptive_name() #Não sei pq, Aqui não funcionou Assim :/
#print(Carro.descrever_BATERIA())
Carro.Bateria_.upgrade_battery() #Meu Erro: Tentei chamar Batery inves de Bateria_ , Porém, Batery esta guardado em Bateria_ :/
Carro.descrever_BATERIA()
Carro.Gasolina_Tk_Cheio()
'''
Quebrei a cabeça, arranquei os cabelos do Cocoroco, mas RESOLVI do MEU Jeito !!
Isso é Uma Grande VITÓRIA
'''
