
class Emplyee:

    def __init__(self, nome: str, sobrenome: str, salario_Anual: float):
        self.Nome = nome
        self.Surname = sobrenome
        self.Sallary = salario_Anual


    def Aumento_Dado(self, soma: float =5000):
        self.Sallary += soma

    def show(self):
        return f"{self.Nome} " \
        f" {self.Sallary}"


H = Emplyee("Dikson", 'Santos', 2000)
H.Aumento_Dado(10000) #Usada a função de dar aumento
print(H.show(), "R$")# ..Ele imprime o Salario 2000+5000 R$. No caso eu adicionei 10.000
#Resultado = 12.000R$

