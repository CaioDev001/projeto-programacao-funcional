import unittest
from sistema_estoque import cadastrar_produto, buscar_por_categoria, calcular_valor_total, aplicar_desconto_categoria

class TestSistemaEstoque(unittest.TestCase):
    
    def setUp(self):
        # Limpa a lista de produtos antes de cada teste
        from sistema_estoque import produtos
        produtos.clear()
        
        # Produtos de teste
        cadastrar_produto("Notebook", "Eletrônicos", 2500.00, 5)
        cadastrar_produto("Mouse", "Eletrônicos", 50.00, 10)
        cadastrar_produto("Caderno", "Papelaria", 15.00, 20)
        cadastrar_produto("Caneta", "Papelaria", 2.50, 200)
    
    def test_cadastrar_produto(self):
        # Testa o cadastro de produto
        from sistema_estoque import produtos
        
        # Verifica quantos produtos temos antes
        produtos_iniciais = len(produtos)
        
        # Cadastra um novo produto
        produto = cadastrar_produto("Teclado", "Eletrônicos", 100.00, 8)
        
        # Verifica se o produto foi cadastrado corretamente
        self.assertEqual(produto['nome'], "Teclado")
        self.assertEqual(produto['categoria'], "Eletrônicos")
        self.assertEqual(produto['preco'], 100.00)
        self.assertEqual(produto['quantidade'], 8)
        
        # Verifica se a lista tem um produto a mais
        self.assertEqual(len(produtos), produtos_iniciais + 1)
    
    def test_buscar_por_categoria(self):
        # Testa a busca por categoria
        eletronicos = buscar_por_categoria("Eletrônicos")
        papelaria = buscar_por_categoria("Papelaria")
        inexistente = buscar_por_categoria("Inexistente")
        
        self.assertEqual(len(eletronicos), 2)
        self.assertEqual(eletronicos[0]['categoria'], "Eletrônicos")
        self.assertEqual(eletronicos[1]['categoria'], "Eletrônicos")
        
        self.assertEqual(len(papelaria), 2)
        
        self.assertEqual(len(inexistente), 0)
    
    def test_calcular_valor_total(self):
        # Testa o cálculo do valor total
        total = calcular_valor_total()

        valor_esperado = 13800.0
        
        self.assertEqual(total, valor_esperado)
    
    def test_aplicar_desconto(self):
        # Testa a aplicação de desconto
        # Primeiro busca os eletrônicos antes do desconto
        eletronicos_antes = buscar_por_categoria("Eletrônicos")
        preco_notebook_antes = next(p['preco'] for p in eletronicos_antes if p['nome'] == "Notebook")
        preco_mouse_antes = next(p['preco'] for p in eletronicos_antes if p['nome'] == "Mouse")
        
        # Aplica 10% de desconto em Eletrônicos
        aplicar = aplicar_desconto_categoria("Eletrônicos", 10)
        resultado = aplicar()
        
        # Verifica a mensagem de retorno
        self.assertEqual(resultado, "Desconto de 10% aplicado em Eletrônicos")
        
        # Busca os eletrônicos depois do desconto
        eletronicos_depois = buscar_por_categoria("Eletrônicos")
        preco_notebook_depois = next(p['preco'] for p in eletronicos_depois if p['nome'] == "Notebook")
        preco_mouse_depois = next(p['preco'] for p in eletronicos_depois if p['nome'] == "Mouse")
        
        # Verifica se os preços foram reduzidos em 10%
        self.assertAlmostEqual(preco_notebook_depois, preco_notebook_antes * 0.9, places=2)
        self.assertAlmostEqual(preco_mouse_depois, preco_mouse_antes * 0.9, places=2)
        
        # Verifica se produtos de outras categorias não foram alterados
        papelaria = buscar_por_categoria("Papelaria")
        preco_caderno = next(p['preco'] for p in papelaria if p['nome'] == "Caderno")
        self.assertEqual(preco_caderno, 15.00)  # Deve permanecer o mesmo

if __name__ == '__main__':
    unittest.main()