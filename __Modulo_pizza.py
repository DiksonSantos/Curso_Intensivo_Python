def make_pizza(size, *toppings): #*toppings -> É uma Tupla
	"""Apresenta a pizza que estamos prestes a preparar."""
	print("\nFazendo Uma Pizza de Tamanho: " + str(size) +
	"-Polegadas Com os Seguintes Recheios: ")
	for topping in toppings:
		print("- " + topping)
		
# -> *Parametro_ Python cria uma Tupla
# -> Em Python uma tupla é imutável e uma lista é mutável. 
# -> **user_info fazem Python criar um dicionário vazio chamado user_info
# -> Um Dicionario pode Receber Listas.

''' https://pt.stackoverflow.com/questions/52799/qual-%C3%A9-a-principal-diferen%C3%A7a-entre-um-tuple-e-um-list
'''

def soma_pizza(Num_1, Num_2):
	soma = Num_1 + Num_2
	print("\nA Quantidade De Pizzas Pedidas Foram: ",soma) #Tentei com o Simbolo de + ao invés de Virgula, mas Não Funciona