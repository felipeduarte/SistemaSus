import unittest
from should_dsl import should

from enfermeiro import Enfermeiro

class Teste_Enfermeiro(unittest.TestCase):

    def setUp(self):
        self.enfermeiro1 = Enfermeiro("joao vitor", "242424" , "auxiliar")

    def test_atributos(self):
        self.enfermeiro1.nome |should| equal_to("joao vitor")
        self.enfermeiro1.matricula |should| equal_to("242424")
        self.enfermeiro1.cargo |should| equal_to("auxiliar")

if __name__ == "__main__":
    unittest.main()
