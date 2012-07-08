import unittest
from should_dsl import should

from paciente import Paciente
from internacao import Internacao
from funcionario import Funcionario
from medico import Medico
from hospital import Hospital
from enfermeiro import Enfermeiro

from datetime import date

class Teste_Paciente(unittest.TestCase):

    def setUp(self):
        self.paciente = Paciente("Pedro", "Masculino", "13/11/1986", "123456")

    def test_atributos(self):
        self.paciente.nome |should| equal_to("Pedro")
        self.paciente.sexo |should| equal_to("Masculino")
        self.paciente.data_de_nascimento |should| equal_to("13/11/1986")
        self.paciente.codigo_do_seguro_social |should| equal_to("123456")
        self.paciente.funcionarios |should| equal_to([])

    def test_calcular_idade(self):
        self.paciente.calcular_idade() |should| equal_to(25)

    


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


class Teste_Enfermeiro(unittest.TestCase):

    def setUp(self):
        self.enfermeiro1 = Enfermeiro("joao vitor", "242424" , "auxiliar")

    def test_atributos(self):
        self.enfermeiro1.nome |should| equal_to("joao vitor")
        self.enfermeiro1.matricula |should| equal_to("242424")
        self.enfermeiro1.cargo |should| equal_to("auxiliar")


class Teste_Medico(unittest. TestCase):

    def setUp(self):
        self.medico1 = Medico("diego", "202020", "pediatra")

    def test_atributos(self):
        self.medico1.nome |should| equal_to("diego")
        self.medico1.matricula |should| equal_to("202020")
        self.medico1.especialidade |should| equal_to("pediatra")

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
