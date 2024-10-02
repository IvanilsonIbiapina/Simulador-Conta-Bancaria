from bd import Banco_de_Dados
from conta_bancaria import ContaBancaria
from cliente import Cliente
from banco import Banco

def main():
    # Criação da instância do banco
    banco = Banco("Banco Simulador")

    while True:
        print("\n--- Menu do Simulador de Banco ---")
        print("1. Adicionar novo cliente")
        print("2. Criar conta para cliente existente")
        print("3. Exibir informações de cliente")
        print("4. Listar todos os clientes")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Digite o nome do cliente: ")
            cpf = input("Digite o CPF do cliente: ")
            banco.adicionar_cliente(nome, cpf)

        elif opcao == '2':
            cpf_cliente = input("Digite o CPF do cliente: ")
            numero_conta = input("Digite o número da nova conta: ")
            banco.criar_conta_para_cliente(cpf_cliente, numero_conta)

        elif opcao == '3':
            cpf_cliente = input("Digite o CPF do cliente: ")
            banco.buscar_cliente(cpf_cliente)

        elif opcao == '4':
            banco.listar_clientes()

        elif opcao == '5':
            print("Saindo do simulador...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    main()
