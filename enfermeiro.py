from funcionario import Funcionario

class Enfermeiro(Funcionario):

    def __init__(self, nome, matricula, cargo):
        Funcionario.__init__(self, nome, matricula)
        self.cargo = cargo
