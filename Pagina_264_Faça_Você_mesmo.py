#9.6 Sorveteria:

class Restaurant():
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type




    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = self.name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = self.name + " is open. Come on in!"
        print("\n" + msg)
'''
restaurant = Restaurant('the mean queen', 'pizza')
print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()
'''

class IceCreamStand(Restaurant):
    def __init__(self,name, cuisine_type="Sorveteria"): #Erro Não coloquei nada em frente cuisine_type
        super().__init__(name, cuisine_type)
        #self.flavors = ["Balnilha", "Banana", "Morango", "Amarena"] #ERRO-> Eu tinha preenchido a lista aqui
        self.flavors = [] #Engraçado que com ou sem esta linha funciona da mesma forma 

    def show_flavours(self): #Erro -> Coloquei um atributo em frente SELF
        FLA = self.flavors
        #print("Sorvetes: ", FLA)
        for S in FLA:
            print("Sorvetes: ", end=" ")
            print("Sabores -> "+S.upper())

Meu_Sorvete = IceCreamStand("Nome")
Meu_Sorvete.flavors = ["Balnilha", "Banana", "Morango", "Amarena"] #A lista Deve ser preenchida aqui, e não la em cima.
Meu_Sorvete.show_flavours()

'''Na maneira de concluir este exercicio eu teria tirado uma nota 7 ou 8, ou talvez 0, 
pelo soft não funcionar corretamente...'''
