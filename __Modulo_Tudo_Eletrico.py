from __Modulo_CAR import Car

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
        if New_Size != self.Volume_Bateria:
            self.Volume_Bateria = New_Size #Atributos de fora desta função devem Ser Inicializados com Self
            #Fim = New_Size
            print("Nova Carga De Bateria = ", New_Size)
    
class ElectricCar(Car):
    """Representa aspectos específicos de veículos elétricos."""
    def __init__(self, make, model, year):
        """Inicializa os atributos da classe pai.
        Em seguida, inicializa os atributos específicos de um carro elétrico"""
        super().__init__(make, model, year) #Herdados
        self.Bateria_ = Batery() #Este Atrib recebe a Class Batery (Que esta com o Valor Defalt de 80)
        self.Nivel_Bateria = 70  #Atrib Exclusivos de carro eletrico.

    def descrever_BATERIA(self):
        '''Cap da Batera'''
        print("This Car has a " + str(self.Nivel_Bateria ) + "-kWhbattery")

    def Gasolina_Tk_Cheio(self):  #REPETINDO O METODO AQUI, ELE SOBREESCREVE O ANTERIOR
        print("Este carro é Eletrico Dhãaarr")