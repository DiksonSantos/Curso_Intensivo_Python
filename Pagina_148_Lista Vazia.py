#requested_toppigs = ['Alaska']
requested_toppigs = str(input('Digite Um Ingrediente: '))
if requested_toppigs:
    for requested_toppigs in requested_toppigs:
        print('Adding  ' + requested_toppigs + '.')
    print('\nFinished Making Your Pizza')
else:
    print('Are You Sure You Want a Plain Pizza??')
# Nesse caso, a lista está vazia, portanto a saída contém uma pergunta para
# saber se o usuário realmente quer uma pizza simples:
# Are you sure you want a plain pizza?
# Se a lista não estiver vazia, a saída mostrará cada ingrediente solicitado
# adicionado à pizza.
