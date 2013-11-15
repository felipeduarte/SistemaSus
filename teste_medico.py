import unittest
from should_dsl import should

from medico import Medico

class Teste_Medico(unittest. TestCase):

    def setUp(self):
        self.medico1 = Medico("diego", "202020", "pediatra")

    def test_atributos(self):
        self.medico1.nome |should| equal_to("diego")
        self.medico1.matricula |should| equal_to("202020")
        self.medico1.especialidade |should| equal_to("pediatra")

if __name__ == "__main__":
    unittest.main()
