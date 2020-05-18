from random import randint

class cliente:
    def __init__(self,nome,documento):
        self.nome = nome
        self.documento = documento

class produto:
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco

class carrinhoCompras:
    def __init__(self,cliente,produtos):
        self.numPedido = randint(100,999)
        self.cliente = cliente
        self.produtos = produtos

    @property
    def valor_carrinho(self):
        total = 0.0
        for produto in self.produtos:
            total += produto.preco

        return total

    def adicionarProduto(self,produto):
        self.produtos.append(produto)

    def removerProduto(self,produto):
        self.produtos.remove(produto)

    def fecharCarrinho(self):
        print(f"Fechando o pedido {self.numPedido}")
        print(f'Valor do carrinho {self.valor_carrinho}')

cliente = cliente('Leonardo','123456')
televisao = produto('Televisao',1000.90)
maquina_de_cafe = produto('Maquina de café', 89.80)
produtos = [televisao,maquina_de_cafe]


carrinho = carrinhoCompras(cliente,produtos)
carrinho.removerProduto(televisao)

computador = produto('Computador',1990.90)
carrinho.adicionarProduto(computador)







print(carrinho.valor_carrinho)
print(carrinho.fecharCarrinho())