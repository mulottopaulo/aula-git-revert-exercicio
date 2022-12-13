class Estoque:
    def __init__(self, loja):
        self.produtos = []
        self.loja = loja

    def calcula_valor_ativos(self):
        sum(produto.valor_custo for produto in self.produtos)