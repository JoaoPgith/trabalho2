from funcionario import Funcionario
from gerente import Gerente
from cliente import cliente
from conta_corrente import ContaCorrente
from conta_poupanca import ContaPoupanca

def main():
    # Criar um cliente
    cliente1 = cliente(nome="João Silva", cpf="123.456.789-00", num_contato="919999999")
    print(f"Cliente criado: {cliente1.nome}, CPF: {cliente1.cpf}, Contato: {cliente1.num_contato}")

    # Criar uma conta poupança para o cliene
    conta_poupanca = ContaPoupanca(numero="001", agencia="1234", cliente=cliente1, saldo=1000.00, historico_transacoes=[], taxa_juros=0.02)
    print("Conta poupança criada com sucesso.")
    # Ver o extrato inicial
    conta_poupanca.extrato()

    # Realizar um depósito
    conta_poupanca.deposito(500.00)
    
    # Realizar um saque
    conta_poupanca.saque(200.00)

    # Aplicar juros
    conta_poupanca.aplicar_juros()

    # Ver o extrato final
    conta_poupanca.extrato()

    # Criar um funcionário
    funcionario1 = Funcionario(nome="Maria Ferreira", cpf="987.654.321-00", num_matricula="F001")
    print(funcionario1.criar_pessoa())

    # Criar um gerente que supervisiona o funcionário
    gerente1 = Gerente(nome="Carlos Pereira", cpf="123.321.123-32", num_matricula="G001", funcionarios=[])
    gerente1.funcionarios.append(funcionario1)
    print(gerente1.criar_pessoa())

    # Mostrar que o gerente tem funcionários
    print(f"O gerente {gerente1.nome} supervisiona o seguinte funcionário:")
    for func in gerente1.funcionarios:
        print(f"Funcionário: {func.nome}, Matrícula: {func.num_matricula}")

if __name__ == "__main__":
    main()
