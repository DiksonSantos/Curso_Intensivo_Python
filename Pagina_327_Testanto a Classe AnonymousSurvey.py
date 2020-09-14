import unittest
from Class_Pesquisa_Anonima_PG_324 import AnonymousSurvey

class TestAnonmynousSurvey(unittest.TestCase):
    """Teste Para a pagina 324"""

    def test_store_single_response(self):
        """Testa se uma única resposta é armazenada de forma apropriada."""
        question = "Que Lingua você aprendeu a falar primeiro?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('Port')

        self.assertIn('Port', my_survey.responses)

unittest.main()


#https://python-guide-pt-br.readthedocs.io/pt_BR/latest/writing/tests.html

"""Rodou Só pelo Prompt Tudo All Right"""
