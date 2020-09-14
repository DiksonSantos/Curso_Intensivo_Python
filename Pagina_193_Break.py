prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    city = input(prompt)

    if city == 'Salto':
        break
    else:
        print('I Would Love to go to ' + city.title())


'''
Um laço que comece com while True executará indefinidamente, a
menos que alcance uma instrução break. _> Ou seja vai ficar perguntando eternamente mesmo que já tenha encontrado o
 que procura. Se é pra fazer varias consultas á uma Lista por exemplo (tudo bem), mas se é apenas para conferir UM dado
 de uma lista, temos que Usar o Break
'''
