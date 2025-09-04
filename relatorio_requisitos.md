# Relatório de Requisitos - Sistema de Gerenciamento de Estoque

## Integrantes da Equipe e Papéis
- William Julian Lemos de Holanda (matrícula: 2314705) - Documentação e Requisitos
- Emmanuel de Oliveira e Silva (matrícula: 2325882) - Documentação e Requisitos
- Vinicius Gabriel da Justa Ximenes (matrícula: 2326167) - Implementação do Código
- Caio Henrique Felix da Silveira (matrícula: 2326320) - Implementação do Código
- Thiago da Silva Tavares (matrícula: 2326278) - Implementação do Código
- Layza Larissa dos Santos (matrícula: 2326311) - Testes e Validação

## Requisitos Funcionais

### RF01 - Cadastrar Produtos
**Descrição:** O sistema deve permitir cadastrar novos produtos no estoque
**Implementação:** Função `cadastrar_produto()` no arquivo `sistema_estoque.py`

### RF02 - Listar Produtos
**Descrição:** O sistema deve listar todos os produtos cadastrados
**Implementação:** Função `listar_produtos()` no arquivo `sistema_estoque.py`

### RF03 - Buscar Produtos por Categoria
**Descrição:** O sistema deve filtrar produtos por categoria
**Implementação:** Função `buscar_por_categoria()` usando **list comprehension**

### RF04 - Calcular Valor Total do Estoque
**Descrição:** O sistema deve calcular o valor total do estoque
**Implementação:** Função `calcular_valor_total()` usando **função de alta ordem** `reduce()`

### RF05 - Aplicar Desconto em Produtos
**Descrição:** O sistema deve aplicar desconto em produtos de uma categoria
**Implementação:** Função `aplicar_desconto_categoria()` usando **closure**

## Requisitos Não-Funcionais

### RNF01 - Interface Simples
**Descrição:** O sistema deve ter interface textual simples e intuitiva
**Implementação:** Função `menu_principal()` no arquivo `sistema_estoque.py`

### RNF02 - Performance
**Descrição:** O sistema deve responder rapidamente às operações
**Implementação:** Uso de funções eficientes e estruturas de dados otimizadas

## Construções de Programação Funcional

### 1. Função Lambda
**Localização:** Função `calcular_valor_total()`
**Uso:** Para somar os valores dos produtos

### 2. List Comprehension
**Localização:** Função `buscar_por_categoria()`
**Uso:** Para filtrar produtos por categoria

### 3. Closure
**Localização:** Função `aplicar_desconto_categoria()`
**Uso:** Para criar uma função que aplica desconto específico

### 4. Função de Alta Ordem
**Localização:** Função `calcular_valor_total()`
**Uso:** `reduce()` para calcular soma total

## Uso de Chatbot
Utilizamos o DeepSeek em situações pontuais, apenas para corrigir erros e revisar o código.