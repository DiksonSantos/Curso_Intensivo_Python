

from MODULOS_Admin_Privileges_ import Admin #Este Modulo Não é o deste Exercicio, Mas com o outro Pedido no exercicio Não Funciona!
#import MODULO_USER

Fulano =Admin("first_name", "last_name", "username", "email", "location")

privilegios = ["alfa", "Bravo"]

Fulano.PRIV.Privileges = privilegios

#print(Fulano.username)

Fulano.PRIV.show_privileges()
Fulano.describe_user() # O arquivo MODULOS_Admin_Privileges_ tem o MODULO_USER já importado






#Dikson.PRIV.Privileges = Dikson_Privilegios # Esta é a Sintaxe para inserir Listas Nesta Classe\Função.



#Continua na PAG 273
