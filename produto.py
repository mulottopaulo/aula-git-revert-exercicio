class Produto:
    def __init__(self, nome, valor_custo, valor_venda, estoque):
        self.nome = nome
        self.valor_custo = valor_custo
        self.valor_venda = valor_venda
        
        self.estoque = estoque
        self.estoque.produtos.append(self)