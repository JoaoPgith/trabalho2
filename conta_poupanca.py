from conta_corrente import ContaCorrente

class ContaPoupanca(ContaCorrente):
    def __init__(self, numero, agencia, cliente, saldo, historico_transacoes,  taxa_juros):
        super().__init__(numero, agencia, cliente, saldo, historico_transacoes)
        self.taxa_juros = taxa_juros
    
    def cria_conta(self):
        return super().cria_conta()
    
    def saque(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente para saque.")
        else:
            self.saldo -= valor
            self.historico_transacoes.append(f'Saque: R${valor:.2f}')
            print(f'Saque de R${valor:.2f} realizado com sucesso')

        
    def deposito(self, valor):
        self.saldo += valor
        self.historico_transacoes.append(f'Saque: R${valor:.2f}')
        print(f'Depósito de R${valor:.2f} realizado com sucesso')

    def extrato(self):
        print(f"Extrato da Conta {self.numero}:")
        print(f"Saldo atual: R${self.saldo:.2f}")

    def aplicar_juros(self):
        juros = self.saldo * self.taxa_juros
        self.saldo += juros
        self.historico_transacoes.append(f"Juros de {juros} aplicados")
        return f"Juros de {juros} aplicados ao saldo"