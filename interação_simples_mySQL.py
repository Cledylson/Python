import mysql.connector

# Conecta ao primeiro banco de dados
db1 = mysql.connector.connect(
    host="localhost",
    user="seu_usuario",
    password="sua_senha",
    database="primeiro_banco"
)

# Cria um cursor para executar as consultas no primeiro banco
cursor_db1 = db1.cursor()

# Executa uma consulta no primeiro banco
cursor_db1.execute("SELECT * FROM tabela_1")

# Imprime os resultados
for x in cursor_db1:
    print(x)

# Conecta ao segundo banco de dados
db2 = mysql.connector.connect(
    host="localhost",
    user="seu_usuario",
    password="sua_senha",
    database="segundo_banco"
)

# Cria um cursor para executar as consultas no segundo banco
cursor_db2 = db2.cursor()

# Executa uma consulta no segundo banco
cursor_db2.execute("SELECT * FROM tabela_2")

# Imprime os resultados
for x in cursor_db2:
    print(x)
