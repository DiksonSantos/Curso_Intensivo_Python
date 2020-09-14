Tipo = str(input('Que Tipo De Pet: '))
Nome_Dele = str(input('Qual Nome Deste bichinho?? '))
#Consegui relacionar a Função com esses INPUTS Uhuu

def describe_pet(animal_type, pet_name):
    '''INFORMAÇ~ES SOBRE OS PETS'''
    print("\nI have a " + animal_type.upper() + ".")
    print("My " + animal_type.title() + "'s name is " + pet_name.title() + ".")
describe_pet(animal_type=Tipo, pet_name=Nome_Dele)       # ->  ESPECIFICANDO AS LIGAÇÕES.

#Parei Em Valores Defausl Pagina -> 211 
