from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, numero, agencia, cliente, saldo):
        self.numero = numero
        self.agencia = agencia 
        self.cliente = cliente
        self.saldo = saldo

    @abstractmethod
    def cria_conta(self):
        pass

    @abstractmethod
    def saque(self):
        pass
    
    @abstractmethod
    def deposito(self):
        pass
    
    @abstractmethod
    def extrato(self):
        pass