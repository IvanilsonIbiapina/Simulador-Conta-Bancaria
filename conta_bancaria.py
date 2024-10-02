class ContaBancaria():
    def __init__(self, numero_conta, titular_id, saldo=0):
        self.__numero_conta = numero_conta
        self.__titular_id = titular_id
        self.__saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido.")
    
    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Erro ao realizar a operação: saldo insuficiente ou valor inválido.")

    def transferir(self, valor, conta_destino):
        if isinstance(conta_destino, ContaBancaria) and 0 < valor <= self.__saldo:
            self.__saldo -= valor
            conta_destino.depositar(valor)
            print(f"Transferência de R${valor:.2f} para a conta {conta_destino.numero_conta} realizada com sucesso.")
        else:
            print("Erro ao realizar a transferência: saldo insuficiente ou conta de destino inválida.")

    def exibir_saldo(self):
        return self.__saldo

    @property
    def numero_conta(self):
        return self.__numero_conta  

    @property
    def titular_id(self):
        return self.__titular_id  
