from datetime import date

class Paciente(object):
    
    def __init__(self, nome, sexo, data_de_nascimento, codigo_do_seguro_social):
        self.nome = nome
        self.sexo = sexo
        self.data_de_nascimento = data_de_nascimento
        self.codigo_do_seguro_social = codigo_do_seguro_social
        self.funcionarios = []
                
    def calcular_idade(self):
        hoje = date.today()
        data_de_aniversario = date(int(self.data_de_nascimento[6:]), int(self.data_de_nascimento[3:5]), int(self.data_de_nascimento[:2]))
        idade = (hoje - data_de_aniversario)
        return int((idade.days)/365)

    def vincular_funcionario(self, objeto_funcionario):
        self.funcionarios.append(objeto_funcionario)
