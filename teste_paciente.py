import unittest
from should_dsl import should

from datetime import date

from paciente import Paciente

class Teste_Paciente(unittest.TestCase):

    def setUp(self):
        self.paciente = Paciente("Pedro", "Masculino", 1989, "123456")

    def test_atributos(self):
        self.paciente.nome |should| equal_to("Pedro")
        self.paciente.sexo |should| equal_to("Masculino")
        self.paciente.ano_de_nascimento |should| equal_to(1989)
        self.paciente.codigo_do_seguro_social |should| equal_to("123456")
        self.paciente.funcionarios |should| equal_to([])

    def test_calcular_idade(self):
        self.paciente.calcular_idade() |should| equal_to(24)

if __name__ == "__main__":
    unittest.main()
