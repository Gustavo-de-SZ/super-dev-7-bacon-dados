from mysql.connector import connect

def executar():
    # # cadastrar_livro()
    # # editar_livro()
    # apagar_livro()
    listar_livro()
    pass



def cadastrar_livro():
    
    titulo = input("digite o nome do livro")
    numero_paginas = input("digite a qtd de paginas")
    autor = input("digite nome autor")
    preco = input("digite preco")
    isbn = input("digite isbn")
    descricao = input("digite descricao")
    
    conexao = connect(
        host ="127.0.0.1",
        port = "3306",
        user = "root",
        password = "admin",
        database = "biblioteca"
        )
    
    cursor = conexao.cursor()
    
    sql = "insert into livros (titulo, numero_paginas, autor, preco, isbn, descricao) VALUES (%s, %s, %s, %s, %s, %s)"
    dados = (titulo, numero_paginas, autor, preco, isbn, descricao)
    
    cursor.execute(sql, dados)
    conexao.commit()
    cursor.close()

def editar_livro():
    id = input("digite o id que deseja alterar")
    titulo = input("digite o nome do livro")
    numero_paginas = input("digite o nuemro de paginas")
    autor = input("digite nome autor")
    preco = input("digite preco")
    isbn = input("digite isbn")
    descricao = input("digite descricao")
    
    conexao = connect(
        host ="127.0.0.1",
        port = "3306",
        user = "root",
        password = "admin",
        database = "biblioteca"
        )
    
    cursor = conexao.cursor()
    
    sql = "UPDATE livros set titulo = %s, numero_paginas = %s, autor = %s, preco = %s, isbn = %s, descricao = %s where id = %s"
    dados = (titulo, numero_paginas, autor, preco, isbn, descricao, id)
    
    cursor.execute(sql, dados)
    conexao.commit()
    cursor.close()


def apagar_livro():
    
    id = input("digite o id do livbro que quer apagar")
    
    conexao = connect(
        host ="127.0.0.1",
        port = "3306",
        user = "root",
        password = "admin",
        database = "biblioteca"
        )
    
    cursor = conexao.cursor()
    
    sql = "DELETE from livros where id = %s"
    dados = (id,)
    
    cursor.execute(sql, dados)
    conexao.commit()
    cursor.close()
    
def listar_livro():
    
    conexao = connect(
        host ="127.0.0.1",
        port = "3306",
        user = "root",
        password = "admin",
        database = "biblioteca"
        )
    
    cursor = conexao.cursor()
    
    cursor.execute("select id, titulo, numero_paginas, autor, preco, isbn, descricao from livros")
    registros = cursor.fetchall()
    
    cursor.close()
    conexao.close()
    
    for registro in registros:
        id = registro[0]
        titulo = registro[1]
        numero_paginas = registro[2]
        autor = registro[3]
        preco = registro[4]
        isbn = registro[5]
        descricao = registro[6]
        print("ID:", id, "TITULO:", "numero de paginas", numero_paginas, autor, preco, isbn, descricao)