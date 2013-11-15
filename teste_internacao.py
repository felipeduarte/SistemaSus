import unittest
from should_dsl import should

from datetime import date

from internacao import Internacao
from paciente import Paciente

class Teste_Internacao(unittest.TestCase):
    def setUp(self):
        self.paciente = Paciente("Pedro", "Masculino", "13/11/1986", "123456")
        self.internacao1 = Internacao(date(2012, 02, 20), date(2012, 02, 25), self.paciente)

    def test_atributos(self):
        self.internacao1.hora_inicio |should| equal_to(date(2012, 02, 20))
        self.internacao1.hora_alta |should| equal_to(date(2012, 02, 25))
        self.internacao1.objeto_paciente |should| equal_to(self.paciente)

if __name__ == "__main__":
    unittest.main()
