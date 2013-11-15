import unittest
from should_dsl import should

from funcionario import Funcionario
from hospital import Hospital

class Teste_Funcionario(unittest.TestCase):

    def setUp(self):
        self.funcionario = Funcionario("Joao", "654321")

    def test_atributos(self):
        self.funcionario.nome |should| equal_to("Joao")
        self.funcionario.matricula |should| equal_to("654321")
        self.funcionario.hospitais |should| equal_to([])

    def test_vincular_hospitais(self):
        hospital1 = Hospital("santa casa", "123456", "Rua Ips")
        self.funcionario.vincular_hospitais(hospital1)
        self.funcionario.hospitais |should| have(1).itens
        hospital2 = Hospital("santa casa", "123456", "Rua Ips")
        self.funcionario.vincular_hospitais(hospital2)
        self.funcionario.hospitais |should| have(2).itens
        hospital3 = Hospital("santa casa", "123456", "Rua Ips")
        self.funcionario.vincular_hospitais(hospital3)
        self.funcionario.hospitais |should| have(3).itens

if __name__ == "__main__":
    unittest.main()
