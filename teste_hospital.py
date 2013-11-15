import unittest
from should_dsl import should

from hospital import Hospital
from funcionario import Funcionario

class Teste_Hospital(unittest.TestCase):
    def setUp(self):
        self.hospital1 = Hospital("santa casa", "123456", "Rua Ips")

    def test_atributos(self):
        self.hospital1.nome |should| equal_to("santa casa")
        self.hospital1.codigo |should| equal_to("123456")
        self.hospital1.endereco |should| equal_to("Rua Ips")
        self.hospital1.funcionarios |should| equal_to([])

    def test_vincular_funcionario(self):
        #vinculando funcionario1:
        funcionario1 = Funcionario("Joao", "654321")
        self.hospital1.vincular_funcionarios(funcionario1)
        self.hospital1.funcionarios |should| have(1).items
        #vinculando funcionario2
        funcionario2 = Funcionario("Pedro", "654321")
        self.hospital1.vincular_funcionarios(funcionario2)
        self.hospital1.funcionarios |should| have(2).items
        #teste_bug
        self.hospital1.vincular_funcionarios(funcionario1)
        self.hospital1.funcionarios |should| have(2).items

    def test_consultar_funcionario(self):
        funcionario1 = Funcionario("Joao", "654321")
        self.hospital1.vincular_funcionarios(funcionario1)
        self.hospital1.consultar_funcionario(funcionario1).nome |should| equal_to("Joao")

if __name__ == "__main__":
    unittest.main()
