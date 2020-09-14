'''
Todas as chamadas a seguir serão adequadas a essa função:
# Um cachorro chamado Willie
describe_pet('willie')
describe_pet(pet_name='willie')
# Um hamster chamado Harry
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')
Cada uma dessas chamadas de função produzirá a mesma saída

'''

def describe_pet(pet_name,animal_type='Dog'): #O DEFAULT SEMPRE DEVE VIR DEPOIS DOS OUTROS PARAMETROS.
    '''  '''
    print("\nI have a " + animal_type.upper() + ".")
    print("My " + animal_type.title() + "'s name is " + pet_name.title() + ".")
describe_pet('Zulu','Rato') 
