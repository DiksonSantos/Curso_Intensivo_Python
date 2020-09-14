
class Restaurant():
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = self.name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = self.name + " is open. Come on in!"
        print("\n" + msg)

    def restaurant(self, gentes):
        self.number_served = gentes
        #return gentes
        quant = gentes
        print("Quantidade de Clientes " , quant)


    def update_clients(self, mileage):  #Da pagina 252
        """
Define o valor de leitura do hodômetro com o valor especificado
Rejeita a alteração se for tentativa de definir um valor menor
para o hodômetro
"""

        if mileage >= self.number_served:
            self.number_served = mileage #
            print("Mais Clientele Chegando ", mileage) #
        else:
            print("Tem Gente Indo Embora Cuidado!!")

    def increment_number_served(self,Mais):
            self.number_served += Mais

restaurant = Restaurant('the mean queen', 'pizza')
print(restaurant.name)
print(restaurant.cuisine_type)

Numeros = int(input("Conv: "))

restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.restaurant(4)
restaurant.update_clients(Numeros)
restaurant.increment_number_served(2)

#  http://pythonclub.com.br/introducao-classes-metodos-python-basico.html

