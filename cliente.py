from bd import Banco_de_Dados 
from conta_bancaria import ContaBancaria

class Cliente():
    def __init__(self, nome, cpf, banco_de_dados) -> None:
        self.__nome = nome
        self.__cpf = cpf
        self.__contas = []
        self.__id = self.__adicionar_cliente(banco_de_dados)

    def __adicionar_cliente(self, banco_de_dados):
        banco_de_dados.adicionar_cliente(self.__nome, self.__cpf)
        cliente = banco_de_dados.buscar_cliente(self.__cpf)
        return cliente[0]

    def criar_conta(self, numero_conta, banco_de_dados):
        nova_conta = ContaBancaria(numero_conta, self.__id)
        self.__contas.append(nova_conta)
        banco_de_dados.criar_conta(numero_conta, self.__id)
        print(f"Conta {numero_conta} criada com sucesso para {self.__nome}")

    def exibir_informacoes(self):
        contas_info = [f"{conta.numero_conta}" for conta in self.__contas]
        print(f"Nome: {self.__nome}, CPF: {self.__cpf}, Contas: {contas_info}")

    @property
    def nome(self):
        return self.__nome 

    @property
    def cpf(self):
        return self.__cpf
