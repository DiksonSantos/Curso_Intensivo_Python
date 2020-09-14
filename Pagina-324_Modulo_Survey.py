'''
class AnonymousSurvey():
    """Coleta respostas anônimas para uma pergunta de uma pesquisa."""
    def __init__(self, question):
        """Armazena uma pergunta e se prepara para armazenar asrespostas."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Mostra a pergunta da pesquisa."""
        print(self.question) #Faltou para o Autor, Colocar Self Aqui

    def store_response(self, new_response):
        """Armazena uma única resposta da pesquisa."""
        self.responses.append(new_response)

    def show_results(self):
        """Mostra todas as respostas dadas."""
        print("Survey results:")
        for response in self.responses:  #E Self Aqui tbm
            print('- ' + response)
'''
class AnonymousSurvey():

    def __init__(self, question): #Aqui Esta em vermelho(problema)
        #Armazena uma pergunta e se prepara para armazenar asrespostas.
        self.question = question
        self.responses = []

    def show_question(self):
        #Mostra a pergunta da pesquisa.
        print(self.question) #Aqui também esta (aparente problema)

    def store_response(self, new_response):
        #Armazena uma única resposta da pesquisa.
        self.responses.append(new_response)

    def show_results(self):
        #Mostra todas as respostas dadas.
        print("Survey results:")
        for response in self.responses:
            print('- ' + response)
