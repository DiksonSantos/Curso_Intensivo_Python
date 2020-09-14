'''
Sobrescrevendo métodos da classe-pai
Qualquer método da classe-pai que não se enquadre no que você estiver
tentando modelar com a classe-filha pode ser sobrescrito. Para isso, defina
um método na classe-filha com o mesmo nome do método da classe-pai
que você deseja sobrescrever. Python desprezará o método da classe-pai e
só prestará atenção no método definido na classe-filha.
'''

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

Fordão = Car("Ford","D-20",1992)
print(Fordão.get_descriptive_name())
Fordão.Gasolina_Tk_Cheio()

print("\n")

Meu_Tesla = ElectricCar("Tesla", "Model-S", 2016)
print(Meu_Tesla.get_descriptive_name())
Meu_Tesla.descrever_BATERIA()
#Meu_Tesla.Gasolina_Tk_Cheio()
#Meu_Tesla.update_odometer(10)
#Meu_Tesla.increment_odometer(120)
#print(Meu_Tesla.read_odometer())

Meu_Tesla.Bateria_.get_range()

Meu_Tesla.Bateria_.Descreve_Bateria() #Instancia.Bateria_Que_Esta_Em_Baixo_De_SUPER.Desc_Bat->ÇQue esta dentro da Class Batery ^^
'''qualquer instância de ElectricCar
agora terá uma instância de Battery criada automaticamente.'''

'''
Parece ser bastante trabalho extra, mas agora podemos descrever a
bateria com quantos detalhes quisermos sem deixar a classe ElectricCar
entulhada
'''

#Continuar Na PAG-263 inicio da folha

#Sobrescrever o conteudo dos Metodos (pais):
# #https://professormarcolan.com.br/como-utilizar-a-heranca-em-python/
