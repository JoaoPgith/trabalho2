from funcionario import Funcionario
#duvida: atributo em formato lista (funcionarios)
class Gerente:
    
    def __init__(self, nome, cpf, num_matricula, funcionarios):
        super().__init__(nome, cpf, num_matricula)
        self.funcionarios = []

        
        
