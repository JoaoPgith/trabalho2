from pessoa import Pessoa

class Funcionario:
    def __init__(self, nome, cpf, num_matricula):
        super().__init__(nome, cpf)
        self.num_matricula = num_matricula
        
