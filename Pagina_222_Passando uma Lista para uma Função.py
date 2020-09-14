#usernames = []
def greet_users(names):
    """Exibe uma saudação simples a cada usuário da lista."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)


Lista_2 = {'Abaco'.upper(), 'XT','I386','PC','MAC'}

usernames = ['hannah', 'ty', 'margot']  #Aparentemente a Lista esta Fora da Função
greet_users(usernames)  # Aqui Foi colocada a Lista como Argumento da Função

greet_users(Lista_2) #Tentei Colocar Este Dicionario como Argumento Junto com a Lista usernames, mas não funciona!
