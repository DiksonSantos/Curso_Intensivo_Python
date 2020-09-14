
def fazer_pizza(*recheios):
    print("Fazendo Pizza Com Os Seguintes Recheios")
    for recheio in recheios:
        print("- " + recheio)


fazer_pizza("Cogumelo")
fazer_pizza("Anchovas","Rabanete","Cebola")

# Essa sintaxe funciona, não importa quantos argumentos a função receba.
