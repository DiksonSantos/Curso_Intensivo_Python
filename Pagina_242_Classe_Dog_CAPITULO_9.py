
class Dog(): #Dog -> Refere-se a Uma Classe
    #Uma forma simples de modelar um Cachorro

    def __init__(self, nome__, idade__):
        #Inicializa os Atributos nome e Idade
        self.nome = nome__
        self.idade = idade__


    def sentar(self):
        #Simula Um Cachorro Sentando em resposta a um Comando.
        print(self.nome.title() + "\tSenta ! ")

    def rolar(self):
        "Simula Cachorro Rolando em Resposta a Um Comando."
        print(self.nome.title() + "\tRolando!")

Nome_Dog = str(input("Nome Do Cachorro: "))
Idade_Dog = int(input("Idade do Pet: "))


Meu_Cão = Dog(Nome_Dog, Idade_Dog) #Meu_Cão -> Refere-se a Uma INSTANCIA   -  Para Acessar as Instancias Nome_Dog & Idade_Dog Use: Meu_Cão.idade & Meu_Cão.nome
#Acredito que Meu_Cão seja Uma Variavel que esta guardando a Classe Dog
print("O Nome do Meu Cachorro é " + Meu_Cão.nome.title() + ".")
print("Meu Cãozinho "+ Meu_Cão.nome.title() +" Tem " + str(Meu_Cão.idade) + " Anos de Idade.") #converte o ovalor do atributo IDADE de my_dog – em uma string.

#Você pode criar tantas instâncias de uma classe quantas forem necessárias.

Meu_Cão.sentar()
Meu_Cão.rolar()

'''Você pode criar tantas instâncias de uma classe quantas forem necessárias, desde que
dê a cada instância um nome de variável único ou que ela ocupe uma única
posição em uma lista ou dicionário.'''

Seu_Cão = Dog("lucy", 3)

print("\nSua Cachorra se Chama  "+ Seu_Cão.nome.title() + "!")
print("A Idade Dela é" + str(Seu_Cão.idade) + "!")
Seu_Cão.sentar()
Seu_Cão.rolar()


#Continuar na Pagina 245
