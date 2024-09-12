from pessoa import Pessoa

class cliente(Pessoa):
    def __init__(self, nome, cpf, num_contato):
        super().__init__(nome, cpf)
        self.num_contato = num_contato
        
