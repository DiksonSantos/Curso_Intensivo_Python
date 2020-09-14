def get_formatted_name(first, last, middle=''):
    """Gera um nome completo formatado de modo elegante."""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()


#O Unico Jeito de funcionar Corretamente com 3 Argumentos é Nomeando-os
#..caso contrario ele recebe exatamente na ordem dos argumentos de fun fir, last, mid.
X = get_formatted_name(first="Gow", middle="Dikson", last="Santos")
print(X)

Y = get_formatted_name("Gow", "Dikson")
print(Y)


"""
J = get_formatted_name('wolfgang', 'mozart', 'amadeus')
print(J)
"""
