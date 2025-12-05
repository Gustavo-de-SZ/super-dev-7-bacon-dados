from mysql.connector import connect

def executar():
    apagar_categoria()
    # editar_categoria()
    # apagar_categoria()
    print('Obrigado')

def criar_categoria():
    
    nome = input("digite o nome da nova categoria")
    print("abrindo conexao")
    
    conexao = connect(
        host ="127.0.0.1",
        port = "3306",
        user = "root",
        password = "admin",
        database = "mercado"
        )
        
    cursor = conexao.cursor()
    
    sql = "INSERT INTO categorias (nome) VALUES (%s)"
    dados = (nome,)
    
    
        
    cursor.execute(sql, dados)
        
    conexao.commit() 
    
    cursor.close()
    
    print("deu certo")

def listar_categorias():
    conexao = connect(
        host = "127.0.0.1",
        port = "3306",
        user = "root",
        password = "admin",
        database = "mercado"
    ) 

    cursor = conexao.cursor()
    
    print("editando categoria")
    cursor.execute("SELECT id, nome FROM categorias")
    
    registros = cursor.fetchall()
    
    cursor.close()
    conexao.close()
    
    for registro in registros:
        id = registro[0]
        nome = registro[1]
        print("ID:", id, "NOME:", nome)
    
   

def editar_categoria():
    listar_categorias()
    
    id = input("digite o id que deseja editar")
    nome = input("digite o novo nome")
    
    conexao = connect(
        host = "127.0.0.1",
        port = "3306",
        user = "root",
        password = "admin",
        database = "mercado"
    ) 
    print("conexao aberta com sucesso")
    cursor = conexao.cursor()
    
    print("editando categoria")
    
    sql = "UPDATE categorias SET nome = %s where id = %s"
    dados =(nome, id)
    cursor.execute(sql, dados)
    
    conexao.commit()
    
    cursor.close()
    conexao.close()
    
    print("categoria editada")

def apagar_categoria():
    listar_categorias()
    
    id = input("digite o id que deseja apagar")
 
    conexao = connect(
        host = "127.0.0.1",
        port = "3306",
        user = "root",
        password = "admin",
        database = "mercado"
    )
    
    print("conexao aberta com sucesso")
    cursor = conexao.cursor()
    
    print("apagando categoria")
    sql = "delete from categorias where id = %s"
    dados = (id,)
    cursor.execute(sql, dados)
    
    conexao.commit()
    
    linhas_afetadas = cursor.rowcount
    if linhas_afetadas == 0:
        print("ID informado inexistente, tente novamente")
    else:
        print("Categoria apagada com sucesso")
        
        
    cursor.close()
    conexao.close()
    
    print("categoria apagada")
    
    
