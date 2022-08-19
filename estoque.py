#Programa de consulta/inserção de registros no Banco de Dados MySQL

#Importando Bibliotecas
import pymysql
import os

# Variáveis
host = '127.0.0.1'
db = 'almoxarifado'
user = 'root'
port = 3306
table = 'material'

#Função conecta ao banco
def conecta_banco(host, db, user, port):
    # conexão com o banco
    try:
        conn = pymysql.connect(host=host, database=db, user=user, port=port)
        #print('Conectado ao Banco \'{}\''.format(db))

        return conn

    except Exception as error:
        print('Error Gerado: ', error)

#Função de consulta
def consulta_banco(conn, table):
    try:
        sql = 'SELECT * FROM {}'.format(table)
        cursor = conn.cursor()
        cursor.execute(sql)
        for record in cursor.fetchall():
            print(record)

    except Exception as error:
        print('Error gerado:',error)

#Função de inserção
def insere_banco(conn,table,nome,quantidade,categoria,localizacao,descricao):
    try:
        sql = 'INSERT INTO {0} (nome,quantidade,categoria,localizacao,descricao) VALUES (\'{1}\',{2},\'{3}\',\'{4}\',\'{5}\');'.format(table,nome,quantidade,categoria,localizacao,descricao)
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    except Exception as error:
        print('Error gerado: ', error)

def encerra_conexao(conn):
    conn.close()

# Chamando a função para conectar com o banco
conexao_banco = conecta_banco(host, db, user, port)

os.system('cls')
print('#'*50)
print('\tBem Vindo ao Estoque do Almoxarifado')
print('#'*50)
print('\n')

while True:
    print('*'*50)
    print('**\t\t\tMENU\t\t\t**')
    print('*'*50)
    print('\t\t1- Consultar materiais')
    print('\t\t2- Inserir um novo material')
    print('\t\t3 - Sair do programa')
    opcao = int(input('\t\tEscolha sua opção:'))
    print('\n')

    if opcao == 1:
        consulta_banco(conexao_banco, table)
        enter = input('\nAperte ENTER para voltar!')
        os.system('cls')
    
    if opcao == 2:
        material = input('Material: ')
        quantidade = int(input('Quantidade: '))
        categoria = input('Categoria: ')
        localizacao = input('Local: ')
        descricao = input('Descrição: ')
        insere_banco(conexao_banco,table, material,quantidade,categoria,localizacao,descricao)
        print('Material inserido!')
        enter = input('\nAperte ENTER para continuar.')
        os.system('cls')
    if opcao == 3:
        encerra_conexao(conexao_banco)
        break

print('FIM')

