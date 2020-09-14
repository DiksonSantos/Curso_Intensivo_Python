#9.1 - Restaurante:
class Restaurant():


    def __init__(self, nome_do_restaurante: str, tipo_de_cozinha: str) -> str:
        self.__Nome = nome_do_restaurante.title() #Tinha me esquecido do Title
        self.__Tipo = tipo_de_cozinha.upper()

    @property
    def descrever_restaurante(self):
        return f"Nome Do Restaurante  {self.__Nome} Tipo De Cozinha: {self.__Tipo}"
        # O metodo do Autor do Livro-> Guardar tudo numa VAR e então Printat a Variavel.


    @property
    def open_restaurant(self):
        return f"O restaurante: {self.__Nome}  Esta: Aberto"


    def Size(self):
        Clientes = 10+12
        print("Quantidade de Clientes Hoje: ", Clientes)


#CHAMANDO A FUNÇÃO, COLOCANDO ELA DENTRO DE UMA VARIAVEL:
Meu_Restaurante = Restaurant(": Lagoa Seca", " Vegetariano")#Aqui é onde inserimos as Informações. Poderiam ser INPUTS tbm

print(Meu_Restaurante.descrever_restaurante, "\n", Meu_Restaurante.open_restaurant)
S = Meu_Restaurante.Size = 45
print("Quantidade de CLientes: ", S)
