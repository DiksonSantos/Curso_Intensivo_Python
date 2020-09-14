def fazer_pizza(tamanho, *Recheios):
    print("\nFazendo Uma Pizza Tamanho: " + str(tamanho) + " Com os Seguintes Recheios: ")
    for recheio in Recheios:

        print("- " + recheio)

fazer_pizza(16, "Peperoni")
fazer_pizza(12, "Cogumelo","Pimentão Verde", 'Queijo Extra')



''' Seguinte: Pelo que Vi, Ele associa a Primeira Informação com o Parametro tamanho, e 
Cria a Tupla que tem o Simbolo * no Segundo Parametro'''
