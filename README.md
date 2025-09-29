# 📦 Sistema de Gerenciamento de Estoque
Um sistema de gerenciamento de estoque desenvolvido em **Python** aplicando conceitos de **Programação Funcional**, como parte da disciplina de Programação Funcional (N704).


## 👥 Equipe e Papéis

| Integrante                          | Matrícula | Papel                       |
|-------------------------------------|-----------|-----------------------------|
| William Julian Lemos de Holanda     | 2314705   | Documentação e Requisitos   |
| Emmanuel de Oliveira e Silva        | 2325882   | Documentação e Requisitos   |
| Vinicius Gabriel da Justa Ximenes   | 2326167   | Implementação do Código     |
| Caio Henrique Felix da Silveira     | 2326320   | Implementação do Código     |
| Thiago da Silva Tavares             | 2326278   | Implementação do Código     |
| Layza Larissa dos Santos            | 2326311   | Testes e Validação          |

## 🚀 Funcionalidades

- **Cadastro de Produtos** – Adicione novos produtos ao estoque  
- **Listagem Completa** – Visualize todos os produtos cadastrados  
- **Busca por Categoria** – Filtre produtos por categoria específica  
- **Cálculo de Valor Total** – Calcule o valor monetário total do estoque  
- **Aplicação de Descontos** – Aplique descontos em categorias específicas  

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+** – Linguagem de programação  
- **Programação Funcional** – Paradigma principal  
- **unittest** – Framework para testes unitários  
- **functools.reduce** – Função de alta ordem para operações acumulativas  

---

## 📋 Conceitos de Programação Funcional Implementados

| Conceito            | Localização               | Função                        | Propósito                               |
|---------------------|---------------------------|-------------------------------|-----------------------------------------|
| Lambda Function     | `sistema_estoque.py:34`   | `calcular_valor_total()`      | Soma acumulada dos valores              |
| List Comprehension  | `sistema_estoque.py:25`   | `buscar_por_categoria()`      | Filtragem de produtos                   |
| Closure             | `sistema_estoque.py:38`   | `aplicar_desconto_categoria()`| Função com estado encapsulado           |
| High-Order Function | `sistema_estoque.py:34`   | `calcular_valor_total()`      | Uso do `reduce()`                       |

---

## 🏗️ Estrutura do Projeto

```
estoque-system/
├── sistema_estoque.py      # Código principal do sistema
├── test_sistema_estoque.py # Testes unitários
├── relatorio_requisitos.md # Documentação de requisitos
└── README.md               # Este arquivo
```

---

## ⚡ Como Executar

### Pré-requisitos
- Python 3.8 ou superior instalado

### Execução do Sistema
```bash
# Clone o repositório
git clone <url-do-repositorio>
cd estoque-system

# Execute o sistema
python sistema_estoque.py
```

### Execução dos Testes
```bash
# Execute todos os testes
python test_sistema_estoque.py

# Ou execute com verbosidade
python -m unittest test_sistema_estoque.py -v
```

---

## 📝 Exemplo de Uso

```
=== SISTEMA DE GERENCIAMENTO DE ESTOQUE ===
1. Cadastrar produto
2. Listar produtos
3. Buscar por categoria
4. Calcular valor total do estoque
5. Aplicar desconto em categoria
6. Sair

Escolha uma opção: 1
Nome do produto: Tablet
Categoria: Eletrônicos
Preço: 1200.00
Quantidade: 8
Produto 'Tablet' cadastrado com sucesso!
```

---

## 🧪 Testes

O sistema inclui testes unitários completos que verificam:

- ✅ Cadastro de produtos  
- ✅ Busca por categoria  
- ✅ Cálculo do valor total  
- ✅ Aplicação de descontos  
- ✅ Integridade dos dados  

**Cobertura de testes:** 100% das funcionalidades principais

---

## 📊 Requisitos Implementados

### Requisitos Funcionais
- RF01 - Cadastrar produtos ✅  
- RF02 - Listar produtos ✅  
- RF03 - Buscar por categoria ✅  
- RF04 - Calcular valor total ✅  
- RF05 - Aplicar desconto ✅  

### Requisitos Não-Funcionais
- RNF01 - Interface simples e intuitiva ✅  
- RNF02 - Performance adequada ✅  

---

## 🔍 Detalhes Técnicos

### Função Lambda
```python
lambda total, prod: total + (prod['preco'] * prod['quantidade'])
```
Uso: Cálculo acumulativo do valor total do estoque

### List Comprehension
```python
[produto for produto in produtos if produto['categoria'] == categoria]
```
Uso: Filtragem eficiente de produtos por categoria

### Closure
```python
def aplicar_desconto_categoria(categoria, percentual_desconto):
    def aplicar_desconto():
        # Implementação do desconto
        return f"Desconto de {percentual_desconto}% aplicado em {categoria}"
    return aplicar_desconto
```
Uso: Encapsulamento da lógica de aplicação de desconto

### Função de Alta Ordem
```python
reduce(lambda total, prod: total + (prod['preco'] * prod['quantidade']), produtos, 0)
```
Uso: Processamento acumulativo sobre a lista de produtos

---

## 🤖 Uso de IA

Utilizamos o **DeepSeek** para correção de erros pontuais e revisão de código e também para estruturar o arquivo `README.md`.
