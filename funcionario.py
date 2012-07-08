from hospital import Hospital

class Funcionario(object):
    
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.hospitais = []

    def vincular_hospitais(self, objeto_hospital):
        self.hospitais.append(objeto_hospital)

