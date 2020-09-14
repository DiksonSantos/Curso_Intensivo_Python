'''
#9.1 - Restaurante:

class Restaurant():


    def __init__(self, nome_do_restaurante, tipo_de_cozinha):
        self.nome = nome_do_restaurante.title() #Tinha me esquecido do Title
        self.tipo = tipo_de_cozinha.upper()


    def descrever_restaurante(self):
        print("Nome Do Restaurante " + self.nome)
        print("Tipo De Cozinha: " + self.tipo  )
        # O metodo do Autor do Livro-> Guardar tudo numa VAR e então Printat a Variavel.



    def open_restaurant(self):
        print("O restaurante" + self.nome.title() + " Esta: Aberto")


    def Size(self):
        Clientes = 10+12
        print("Quantidade de Clientes Hoje: " , Clientes)


#CHAMANDO A FUNÇÃO, COLOCANDO ELA DENTRO DE UMA VARIAVEL:
Meu_Restaurante = Restaurant(": Lagoa Seca"," Vegetariano")#Aqui é onde inserimos as Informações. Poderiam ser INPUTS tbm

print("Nome Do Restaurante" + Meu_Restaurante.nome )
print("Tipo" + Meu_Restaurante.tipo)



Meu_Restaurante.open_restaurant() # Restaurante Aberto
Meu_Restaurante.descrever_restaurante() #Contém Nome e Tipo
Meu_Restaurante.Size() #Quantidade de Clientes

#Acredito que esta certo.

'''

#________________________

'''
#9.2 – Três restaurantes:

class Restaurant():


    def __init__(self, nome_do_restaurante, tipo_de_cozinha):
        self.nome = nome_do_restaurante.title() #Tinha me esquecido do Title
        self.tipo = tipo_de_cozinha.upper()


    def descrever_restaurante(self):
        print("Nome Do Restaurante " + self.nome) #Lembrando que estas STRINGS poderiam ser INPUTs que se combinariam com Os selfs
        print("Tipo De Cozinha: " + self.tipo  )
        #msg = self.nome + " Tem\Serve Uma Ótima " + self.tipo + "."
        #print("\n" + msg)
        # O metodo do Autor do Livro-> Guardar tudo numa VAR e então Printat a Variavel.



    def open_restaurant(self):
        print("O restaurante" + self.nome.title() + " Esta: Aberto")


#O Nome destes 3 restaurantes a baixo Sõ o que se pode chamar de Instancias

Veg_Restaurant = Restaurant("Lagoa Seca", "Cozinha Veg")     
Veg_Restaurant.descrever_restaurante()

mean_queen = Restaurant('the mean queen', 'pizza')
mean_queen.descrever_restaurante()

mongo_thai = Restaurant("mango thai", "Comida tailandesa")
mongo_thai.descrever_restaurante()
'''

'''
#9.3 – Usuários:

class User():

    def __init__(self, First_Nome, Last_Nome, Age, Weight, Etnic):
        self.nome = First_Nome
        self.Ultimo_Nome = Last_Nome
        self.Idade = Age
        self.Peso = Weight
        self.Etnia = Etnic


    def describe_user(self):
        print()
'''
