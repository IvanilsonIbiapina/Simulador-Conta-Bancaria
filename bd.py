import sqlite3

class Banco_de_Dados():
    def __init__(self, db_name='banco.db'):
        # Cria a conexão com o banco de dados
        self.conexao = sqlite3.connect(db_name)
        self.cursor = self.conexao.cursor()
        self.criar_tabelas()

    def criar_tabelas(self):
        # Cria a tabela de clientes
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cpf TEXT NOT NULL UNIQUE
            )
        ''')

        # Cria a tabela de contas
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS contas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                numero_conta TEXT NOT NULL,
                titular_id INTEGER,
                saldo REAL DEFAULT 0,
                FOREIGN KEY (titular_id) REFERENCES clientes (id)
            )
        ''')

        self.conexao.commit()

    def adicionar_cliente(self, nome, cpf):
        self.cursor.execute('''
            INSERT INTO clientes (nome, cpf) VALUES (?, ?)
        ''', (nome, cpf))
        self.conexao.commit()

    def buscar_cliente(self, cpf):
        self.cursor.execute('''
            SELECT * FROM clientes WHERE cpf = ?
        ''', (cpf,))
        return self.cursor.fetchone()

    def listar_clientes(self):
        self.cursor.execute('''
            SELECT * FROM clientes
        ''')
        return self.cursor.fetchall()  # Retorna todos os clientes cadastrados

    def criar_conta(self, numero_conta, titular_id):
        self.cursor.execute('''
            INSERT INTO contas (numero_conta, titular_id) VALUES (?, ?)
        ''', (numero_conta, titular_id))
        self.conexao.commit()

    def buscar_conta(self, numero_da_conta):
        self.cursor.execute('''
            SELECT * FROM contas WHERE numero_conta = ?
        ''', (numero_da_conta,))
        return self.cursor.fetchone()  # Retorna a conta encontrada

    def atualizar_saldo(self, numero_conta, novo_saldo):
        self.cursor.execute('''
            UPDATE contas SET saldo = ? WHERE numero_conta = ?
        ''', (novo_saldo, numero_conta))
        self.conexao.commit()

    def fechar_conexao(self):
        self.conexao.close()
