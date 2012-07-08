from funcionario import Funcionario

class Medico(Funcionario):

    def __init__(self, nome, matricula, especialidade):
        Funcionario.__init__(self, nome, matricula)
        self.especialidade = especialidade
