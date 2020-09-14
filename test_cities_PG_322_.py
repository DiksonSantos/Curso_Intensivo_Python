
import unittest

#from city_functions_Pg322 import get_formatted_name
'''
class Testar_Fun_Pais(unittest.TestCase):
	#Testar a Função City_functions

	def test_city_Countries(self):
		testa_aqui = get_formatted_name('Minas Gerais', 'Brasil')
		self.assertEqual(testa_aqui, 'Minas Gerais Brasil')

unittest.main()



#OK Funcionou !
'''

'''
from city_functions_Pg322 import Population

class Testar_Population_Func(unittest.TestCase):
	#Testar O Novo Metodo da Classe city_fun...

	def test_Population(self):
		Novo_Teste = Population('SP', 'Sp','2M')
		#self.assertEqual(Novo_Teste, 'ST_CATARINA BLUMENAU')
		self.assertEqual(Novo_Teste, 'SP SP 2M')

unittest.main()
#Popu = Population('St_Catarina', 'Blumenau')
'''

from city_functions_Pg322 import get_formatted_name

class Testar_Formata_Nome(unittest.TestCase):
	'testar Formatador de Nome Cidade Estado ...'
	def Test_Formato_Nomes(self):
		Testando = get_formatted_name('Salto', 'SP')
		#self.assertAlmostEqual('Salto SP aqui')
		self.assertEqual(Testando, 'Salto SP') #Se rodar sem a Variavel 'Testando' , também funciona normal (??)

#unittest.main()


#CONTINUA NA PAG - 323

