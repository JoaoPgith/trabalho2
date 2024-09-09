
from funcionario import Funcionario
from gerente import Gerente
from cliente import cliente
from conta_corrente import ContaCorrente
from conta_poupanca import ContaPoupanca

cliente1= cliente('Joâo', '123.321.123.12', '97564-7363')
funcionario1 = Funcionario('Samuel', '786.876.678-87', '765432')
gerente1 = Gerente('Mateus', '456.654.456-65', '123456',[funcionario1] )
