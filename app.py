import pyodbc
# Drive - Drive
# Server - Server
# Database - Nome do Banco de Dados
dados_conexao = (
    "DRIVER={SQLite3 ODBC Driver};SERVER=localhost;DATABASE=./database/projeto_compras.db;Trusted_connection=yes")


# Criando a conexão
conexao = pyodbc.connect(dados_conexao)

print("Conectado com sucesso!")

# cursor - Ferramenta para executar os comandos em SQL
cursor = conexao.cursor()

# Selecionando a tabela do banco de dados
cursor.execute("SELECT * FROM usuarios")
# Passar os dados para a variável
valores = cursor.fetchall()

produtos = cursor.execute("SELECT * FROM produtos").fetchall()

for i in valores:
    for k in i:
        print(k)

print(produtos)

# Inserindo informações no banco de dados
dados_usuario = ("ismaelsoares", "soberano456")
cursor.execute(
    "INSERT INTO usuarios (nome, senha) VALUES (?, ?)", dados_usuario)
conexao.commit()  # Gravando no Banco de Dados

cursor.execute("SELECT * FROM usuarios")

valores = cursor.fetchall()

print(valores)

# Fechar o cursor e a conexão
cursor.close()
conexao.close()
