'''
#8.12 Sanduiches:
def Fazer_Sanduiche(Pão_Tipo,**Extras):
    Sanduba = {}
    Sanduba["Tipo de Pão"] = Pão_Tipo #Organizar, Quem é Chave, Quem é Valor.

    for Paes, X_Tras in Extras.items():
        Sanduba[Paes] = X_Tras  #Acredito que Nesta Linha se Define a Forma\Sequencia Como as Informações Serão Organizadas (chave: Valor)
    return Sanduba
print("Escolha Tipo De Pão Para Todos Os Sanduiches Desta Rodada ")
Pães = str(input("Qual Pão?: "))
#Forma_Pão = str(input("Pão Redondo Ou Comprido? "))


Lanche = Fazer_Sanduiche(Pão_Tipo=Pães, Recheio ="Maionese", Queijo = "Cheddar")
Lanche_2 = Fazer_Sanduiche(Pão_Tipo=Pães, Recheio ="Molho", Queijo = "Suiço")
Lanche_3 = Fazer_Sanduiche(Pão_Tipo=Pães, Recheio ="Marmelada", Queijo = "Minas")

print("Seus 3 Lanches:\n{} \n {} \n {}".format(Lanche,Lanche_2,Lanche_3)  )
#print()
#print(Lanche)

#OK We Did It
'''

#8.13 Já Fiz:



#8.14 Carros:
def make_car(Marca ,Modelo  ,**More_Inf ):
    Carro = {}
    Carro  ["Marca"] = Marca
    Carro  ["Modelo"] = Modelo

    for type, mod in More_Inf.items():
        Carro[type] = mod
    return Carro

print(make_car("Niponic", "Subaru", Cor = "Silver", Pacote = "Unknown", Tipo = "Racer")) # Funciona Assim

Res = make_car("Wolks",  "Merceds", Cor = "Azul", Pacote = "Desconhecido", Tipo = "Tracker", Uso = "Carro de Passeio") #Funciona Assim também

print(Res)
print(Res.keys()) #Acredito que: Para fazermos alterações assim, precisamos guardar a função com sues argumentos numa Variavel.
#OK WE DID IT !


