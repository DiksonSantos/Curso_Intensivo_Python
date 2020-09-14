
# _MODULO_Admin.py  -> Contém todos os Modulos

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
