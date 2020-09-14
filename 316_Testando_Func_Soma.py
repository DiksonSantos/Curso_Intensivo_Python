import unittest
from Soma import soma


class Nome_Test_Soma(unittest.TestCase):
    """Testa Função Soma"""

    def test_aqui(self):
        "Esta Somando?"
        Somando = soma(2,2)
        self.assertEqual(Somando, 4)



unittest.main()

"""
 SÓ FUNCIONOU QUANDO DIGITEI NO TERMINAL:
$ python 316_Testando_Func_Soma.py
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
"""
