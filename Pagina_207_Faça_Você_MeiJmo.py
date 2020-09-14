'''
#8.1
def display_message(automate):
    print('Autometização Interna de Codigos é o que estamos Aprendendo aqui Uhu '+automate) #A palavra automate:
display_message('That´s It') #É o que você Digitar AQUI. Ou seja, é uma Variavél que armazena o que for digitado aqui.

#We didi it
'''

'''
#8.2
def favorite_book(BOOK):
    print('Um Dos Meus Livros Favoritos é '+BOOK)
    
favorite_book('A Estrada Para o Futuro de Bill Gates')
'''


Tipo = str(input('Que Tipo De Pet: '))
Nome_Dele = str(input('Qual Nome Deste bichinho?? '))
#Consegui relacionar a Função com esses INPUTS Uhuu

def describe_pet(animal_type, pet_name):
    '''INFORMAÇ~ES SOBRE OS PETS'''
    print("\nI have a " + animal_type.upper() + ".")
    print("My " + animal_type.title() + "'s name is " + pet_name.title() + ".")
describe_pet(Tipo, Nome_Dele)
describe_pet('Toninho','Pera')
