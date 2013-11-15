from time import localtime

class Paciente(object):
    
    def __init__(self, nome, sexo, ano_de_nascimento, codigo_do_seguro_social):
        self.nome = nome
        self.sexo = sexo
        self.ano_de_nascimento = ano_de_nascimento
        self.codigo_do_seguro_social = codigo_do_seguro_social
        self.funcionarios = []
                
    def calcular_idade(self):
        idade = 0
        data_completa = localtime()
        ano_atual = data_completa[0]
        idade = ano_atual - self.ano_de_nascimento
        return idade

    def vincular_funcionario(self, objeto_funcionario):
        self.funcionarios.append(objeto_funcionario)
