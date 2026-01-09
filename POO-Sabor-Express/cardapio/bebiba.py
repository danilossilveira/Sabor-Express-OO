from cardapio.cardapio_item import Cardapio
class Bebida(Cardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self.tamanho = tamanho

    def __str__(self):
        return (f' Nome: {self._nome}\n Preço: {self._preco}\n Tamanho: {self.tamanho}\n')    
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.5)