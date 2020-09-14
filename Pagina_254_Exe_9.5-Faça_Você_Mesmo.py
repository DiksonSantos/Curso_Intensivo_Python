class User():

    def __init__(self, First_name, Last_name, User_Name, email, location ):
        '''Inicializar Usuario.'''
        self.first_name = First_name.title()
        self.last_name = Last_name.title()
        self .user_name = User_Name.upper()
        self.email = email
        self.location = location
        self.login_attempts = 0

    def descrever_User(self):
        '''Mostra as Informações do Usuario'''
        print('\n' + self.first_name + "" + self.last_name)
        print("  Username: " + self.user_name)
        print("  Email: " + self.email)
        print("  Location: " + self.location)

    def greet_user(self):
        '''Cumprimenta Usuario'''
        print("\nBem Vindo de Volta  " + self.user_name + "!")

    def increment_login_attempts(self): #Pelo que vi, se não tiver este Self aqui, não adianta por o logo a baixo (nada funciona)
         self.login_attempts += 1 #Toda vez que INCREMENT_LOGIN for chamada ela guarda\registra +1

    def reset_attempts(self):
        self.login_attempts = "Zerou"  #Mostra (neste caso a Atring ZEROU #Podia ser Um Numero aqui tbm...


Gow = User("Dikson", " Santos", "DK", "Dikson_Santos@outlook.com","SP")
Gow.descrever_User()
Gow.greet_user()

#print("Fazendo 3 tentativas de Login")
Gow.increment_login_attempts()
Gow.increment_login_attempts()
Gow.increment_login_attempts()
print("Tentativa de Login: " + str(Gow.login_attempts))



DS = User("Gow", " R. Santos", "Godovar", "Diksonnn@gmail.com","Salto-SP")
DS.descrever_User()
DS.greet_user()

DS.increment_login_attempts()
DS.increment_login_attempts()
DS.increment_login_attempts()
print("Tentou Logar " + str(DS.login_attempts) + " Vezes")

Gow.reset_attempts()
DS.reset_attempts()
print("\nReset Tentativas User Gow "+ str(Gow.login_attempts))
print("\nReset Tentativas User DS " + str(DS.login_attempts))
#print("Resetando tentativas de Login para {} e {}".format(str(Gow.login_attempts()), str(DS.login_attempts())))


