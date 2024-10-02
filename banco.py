from cliente import Cliente
from bd import Banco_de_Dados

class Banco:
    def __init__(self, nome):
        self.__nome = nome  # Atributo privado
        self.__clientes = []  # Lista de clientes cadastrados no banco
        self.db = Banco_de_Dados()  # Instância do banco de dados

    def adicionar_cliente(self, nome, cpf):
        # Verifica se o cliente já existe no banco de dados
        cliente_existente = self.db.buscar_cliente(cpf)
        if cliente_existente:
            print(f"Cliente com CPF {cpf} já está cadastrado.")
        else:
            # Cria um novo cliente e o adiciona à lista de clientes
            novo_cliente = Cliente(nome, cpf, self.db)  # Passando a instância do banco de dados
            self.__clientes.append(novo_cliente)
            print(f"Cliente {nome} com CPF {cpf} adicionado com sucesso.")

    def criar_conta_para_cliente(self, cpf, numero_conta):
        # Busca o cliente pelo CPF
        cliente = next((c for c in self.__clientes if c.cpf == cpf), None)
        if cliente:
            # Cria uma nova conta associada ao cliente
            cliente.criar_conta(numero_conta, self.db)  # Passando a instância do banco de dados
        else:
            print(f"Cliente com CPF {cpf} não encontrado.")

    def buscar_cliente(self, cpf):
        # Busca um cliente pelo CPF e exibe suas informações
        cliente = next((c for c in self.__clientes if c.cpf == cpf), None)
        if cliente:
            cliente.exibir_informacoes()
        else:
            print(f"Cliente com CPF {cpf} não encontrado.")

    def listar_clientes(self):
        # Lista todos os clientes cadastrados no banco
        if self.__clientes:
            for cliente in self.__clientes:
                cliente.exibir_informacoes()
        else:
            print("Nenhum cliente cadastrado no banco.")

    @property
    def nome(self):
        return self.__nome  # Método getter para acessar o nome do banco
