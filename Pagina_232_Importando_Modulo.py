import __Modulo_pizza # import nome_da_função.Função_Especifica_Dentro_Do_Modulo

pizza_1 = int(input("Quantas Pizzas 01-? "))
pizza_2 = int(input("Quantas Pizzas 01-? "))

__Modulo_pizza.make_pizza(16, "Peperoni")
__Modulo_pizza.make_pizza(12, "Cogumelos", "Pimentão Verde", "Queijo Extra")
__Modulo_pizza.soma_pizza(pizza_1, pizza_2)

from __Modulo_pizza import soma_pizza, make_pizza            # Desta maneira voce pode Importar todas as Funções de Um Modulo Numa Unica Linha


