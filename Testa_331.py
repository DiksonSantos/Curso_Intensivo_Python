import unittest

from Pagina_331_Faca_Voce_Mesmo import Emplyee

class Test_Empregado(unittest.TestCase):
    """Testa a função empregados"""


    def setUp(self):  #AQUI NÃO PODE SER QUALQUER NOME, TEM QUE SER 'setUp' para ele herdar da Classe mãe. Se não da pau.
        """Make an employee to use in tests.
        método setUp() serve para criar instâncias/Objetos Neste
        caso para testar as funções do outro Arquivo/Modulo"""
        self.Dikson = Emplyee('dikson', 'santos', 65000)

    def test_give_default_raise(self):
        """Test that a default raise works correctly."""
        self.Dikson.Aumento_Dado()
        self.assertEqual(self.Dikson.Sallary, 70000)

    def test_fun_aumento(self):
        """Se Dikson.Aumento = 10.000 , por que o Resultado Correto tem que ser 7.500 ???"""
        self.Dikson.Aumento_Dado(10000)
        self.assertEqual(self.Dikson.Sallary, 75000)
        #self.assertEqual(self.Dikson.Aumento_Dado(), 17000)

unittest.main()

