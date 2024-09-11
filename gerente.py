from funcionario import Funcionario
#duvida: atributo em formato lista (funcionarios)
class Gerente(Funcionario):
    
    def __init__(self, nome, cpf, num_matricula, funcionarios):
        super().__init__(nome, cpf, num_matricula)
        self.funcionarios = []

    def criar_pessoa(self):
        return f"Gerente {self.nome}, CPF {self.cpf}, Matrícula {self.num_matricula}"
        
        
