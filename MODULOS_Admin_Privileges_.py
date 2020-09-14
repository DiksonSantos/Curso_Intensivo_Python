#Veja: a class Admin(User):  Para funcionar precisa importar o 'user' , assim da pra conectar as classes mesmo elas não estando no mesmo arquivo.

from MODULO_USER import User  # A linha que quase me deixou Louco em 04-01-2019

class Admin(User): #-> FAZ COM QUE METODOS DA CLASSE USER SEJAM HERDADOS OU POSSAM SER USADOS COM AS INSTANCIAS DESTA AQUI:
    """A user with administrative privileges."""

    def __init__(self ,first_name, last_name, username, email, location): #Isso aqui é chamado de metodo construtor
        #self.Prime_Nom = Primeiro
        """Initialize the admin."""
        super().__init__(first_name, last_name, username, email, location) #Inicializa os atributos da classe-pai
        #self.etnia = American
        '''A função super()  é uma função especial que ajuda Python a criar
conexões entre a classe-pai e a classe-filha. Essa linha diz a Python para
chamar o método __init__() da classe-pai , que confere
todos os atributos da classe-pai a Classe_Filha. '''


        # Inicializa Uma Lista Vazia De privileges.
        #FOI PRECISO CRIAR NESTE EXE UMA LISTA VAZIA P/ DEPOIS CRIAR UMA CLASSE Q LIDE COM LISTAS.
        self.PRIV = Privileges()


class Privileges():

    """Uma CLasse Para Armazenar Os Privilegio."""
    def __init__(self, privileges=[]): #Assim o Atributo recebido é uma Lista Vazia
        self.Privileges = privileges #Inicializa Uma Var Interna, que Recebe A Var Do Parametro[Que é Uma Lista]

    def show_privileges(self):
        print("\nPrivileges:")
        if self.Privileges: #Com 'P' maiusculo esta é a Var Interna que recebeu o Parametro
            for privilege in self.Privileges: #Esta também.
                print("- " + privilege) #Se quiser tudo na mesma linha -> (priv, end="")
        else:
            print("- This user has no privileges.") #Caso a Lista Esteja vazia ...
