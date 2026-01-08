from cardapio.cardapio_item import Cardapio
class Comida(Cardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self.descricao = descricao

    def __str__(self):
        return (f' Nome: {self._nome}\n Preço: {self._preco}\n Descrição: {self.descricao}\n')      