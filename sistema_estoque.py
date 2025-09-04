from functools import reduce

# Lista de produtos
produtos = []

# RF01 - Cadastrar produto
def cadastrar_produto(nome, categoria, preco, quantidade):
    # Cadastra um novo produto no sistema
    produto = {
        'id': len(produtos) + 1,
        'nome': nome,
        'categoria': categoria,
        'preco': preco,
        'quantidade': quantidade
    }
    produtos.append(produto)
    return produto

# RF02 - Listar produtos
def listar_produtos():
    # Lista todos os produtos cadastrados
    return produtos

# RF03 - Buscar por categoria (usando LIST COMPREHENSION)
def buscar_por_categoria(categoria):
    # Filtra produtos por categoria usando list comprehension
    
    # LIST COMPREHENSION
    return [produto for produto in produtos if produto['categoria'] == categoria]

# RF04 - Calcular valor total (usando FUNÇÃO DE ALTA ORDEM e LAMBDA)
def calcular_valor_total():
    # Calcula o valor total do estoque usando reduce e lambda
    if not produtos:
        return 0.0
    
    # Função reduce e LAMBDA
    return reduce(lambda total, prod: total + (prod['preco'] * prod['quantidade']), produtos, 0)

# RF05 - Aplicar desconto (usando CLOSURE)
def aplicar_desconto_categoria(categoria, percentual_desconto):
    # Cria uma closure para aplicar desconto em produtos de uma categoria
    def aplicar_desconto():
        # Closure que aplica desconto nos produtos da categoria especificada
        desconto = percentual_desconto / 100
        for produto in produtos:
            if produto['categoria'] == categoria:
                produto['preco'] *= (1 - desconto)
        return f"Desconto de {percentual_desconto}% aplicado em {categoria}"
    
    return aplicar_desconto

# Função principal
def menu_principal():
    # Menu interativo 
    while True:
        print("\n=== SISTEMA DE GERENCIAMENTO DE ESTOQUE ===")
        print("1. Cadastrar produto")
        print("2. Listar produtos")
        print("3. Buscar por categoria")
        print("4. Calcular valor total do estoque")
        print("5. Aplicar desconto em categoria")
        print("6. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            nome = input("Nome do produto: ")
            categoria = input("Categoria: ")
            preco = float(input("Preço: "))
            quantidade = int(input("Quantidade: "))
            produto = cadastrar_produto(nome, categoria, preco, quantidade)
            print(f"Produto '{produto['nome']}' cadastrado com sucesso!")
            
        elif opcao == '2':
            print("\n=== LISTA DE PRODUTOS ===")
            for prod in listar_produtos():
                print(f"{prod['id']}. {prod['nome']} - {prod['categoria']} - R${prod['preco']} - {prod['quantidade']} unidades")
                
        elif opcao == '3':
            categoria = input("Categoria para buscar: ")
            encontrados = buscar_por_categoria(categoria)
            print(f"\nProdutos na categoria '{categoria}':")
            for prod in encontrados:
                print(f"- {prod['nome']} - R${prod['preco']}")
                
        elif opcao == '4':
            total = calcular_valor_total()
            print(f"\nValor total do estoque: R${total:.2f}")
            
        elif opcao == '5':
            categoria = input("Categoria para desconto: ")
            percentual = float(input("Percentual de desconto: "))
            
            # Closure
            aplicar = aplicar_desconto_categoria(categoria, percentual)
            resultado = aplicar()
            print(resultado)
            
        elif opcao == '6':
            print("Saisndo do sistema...")
            break
            
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    # Produtos de exemplo
    cadastrar_produto("Notebook", "Eletrônicos", 2500.00, 10)
    cadastrar_produto("Mouse", "Eletrônicos", 50.00, 30)
    cadastrar_produto("Caderno", "Papelaria", 15.00, 100)
    cadastrar_produto("Caneta", "Papelaria", 2.50, 200)
    
    menu_principal()