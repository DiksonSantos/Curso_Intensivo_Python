
Nome_Do_Bicho = str(input('Nome Do animal '))
#Tipo = str(input('Tipo? '))   # Se voce Preciona ENTER aqui, ou seja, Não digitou NADA , ele usará o Valor DEFAULT Que é DOG.
#A Linha a cima não funciona-> Ele sempre Escreve DOG de qualquer Jeito :/

def describe_pet( pet_name,animal_type=''): #O DEFAULT SEMPRE DEVE VIR DEPOIS DOS OUTROS PARAMETROS.
    ''' Descobri depois que-> Para deixar Um Valor Opcinal deve-se deixar a String Vazía em frente ao PARAMETRO, ao invés de DOG -> '' Mas é preciso outras Adiçoes tbm     '''
    print("\nI have a " + animal_type.upper() + ".")
    print("My " + animal_type.title() + "'s name is " + pet_name.title() + ".")
describe_pet(pet_name=Nome_Do_Bicho, animal_type=''  )       # ->  O modo mais simples de usar essa função agora é fornecer apenas onome de um cachorro na chamada da função

'''Se Houver um argumento explícito para animal_type foi especificado como:animal_type='Passaro', 
Python ignorará o valor default do parâmetro.
-> No meu codigo aqui Eu deixei para ele escolher entre o valor Default e o INPUT, ele sempre escolhe o Valor Default
'''

'''
ANIMAL_TIPE no Print esta definido como DOG nos Parametros ANIMAL_TIPE Contme DOG


O único argumento fornecido é -> pet_name=Nome_Do_Bicho portanto ele é associado ao
primeiro parâmetro da definição da função, que é pet_name.
Como nenhum argumento foi fornecido para animal_type, Python usa o valor default, que é 'dog'.
'''
