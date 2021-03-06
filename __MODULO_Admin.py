class User():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        #self.america = American
        self.login_attempts = 0  #ESTA É A UNICA VARIAVEL INTERNA (OU LOCAL) QUE NÃO É TAMBÉM UM ARGUMENTO DA DEF

    def describe_user(self):
        """Display a summary of the user's information."""
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location) #OS TRECHOS DESTE TIPO APENAS PRINTAM AS VARIAVEIS SELECIONADAS

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print("\nWelcome back, " + self.username + "!") #OUTRO TIPO DE DEF PARA PRINTAR

    def increment_login_attempts(self):
        """Increment the value of login_attempts."""
        self.login_attempts += 1  #TODA VEZ QUE FOR CHAMADA INCREMENTA 1

    def reset_login_attempts(self):
        """Reset login_attempts to 0."""
        self.login_attempts = 0 #TODA VEZ QUE CHAMADA ZERA O VALOR DA DE CIMA. A MESMA VAR INTERNA DE CIMA ESTA EM USO.


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
