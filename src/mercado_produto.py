from src.repositorios import mercado_produto_repositorio


def executar():
    listar_produtos()
    
    
    
    
def criar_produto():
    nome = input("digite o nome do novo produto : ")
    id_categoria = int(input("digite o id da categoria"))
    
    mercado_produto_repositorio.cadastrar(nome, id_categoria)
    print("pdotuo criado")
    

def apagar_produto():
    id = int(input("digite o id"))
    linhas_afetadas = mercado_produto_repositorio.apagar(id)
    
    if linhas_afetadas:
        print("produto apagaod")
    else: 
        print("deu ruim")
        

def listar_produtos():
   produtos = mercado_produto_repositorio.obter_todos()
   print("codigo nome categoria")
   for produto in produtos:
       print(produto["id"], produto["nome"], produto["categoria"]["nome"])