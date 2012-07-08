class Hospital(object):

    def __init__(self, nome, codigo, endereco):
        self.nome = nome
        self.codigo = codigo
        self.endereco = endereco
        self.funcionarios = []

    def vincular_funcionarios(self, objeto_funcionario):
        if self.consultar_funcionario(objeto_funcionario) == None:
            self.funcionarios.append(objeto_funcionario)

    def consultar_funcionario(self, objeto_funcionario):
        for funcionario in self.funcionarios:
            if funcionario == objeto_funcionario:
                return objeto_funcionario
        return None

    
