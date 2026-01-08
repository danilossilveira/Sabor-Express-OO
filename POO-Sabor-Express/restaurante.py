from cardapio.cardapio_item import Cardapio

class Restaurante(Cardapio):
    restaurantes = []
    def __init__ (self, nome, categoria):
        self._nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f' Nome: {self._nome}\n Categoria: {self.categoria}\n Estado: {self.ativo}\n'
    @classmethod
    def listar_restaurante(cls):
        print('Nome'.ljust(20),'|Categoria'.ljust(22),'|Estado')
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante.categoria.ljust(20)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return 'ativado' if self._ativo else 'desativado'
    
    def alterar_estado(self):
        self._ativo = not self._ativo


    def adicionar_no_cardapio(self, item):
        if isinstance(item, Cardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f'Cardapio do restaurante {self._nome}')
        for i,item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'descricao'):
                mensagem_comida = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Descrição: {item.descricao}'
                print(mensagem_comida)
            else:
                mensagem_bebida = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Tamanho: {item.tamanho}'
                print(mensagem_bebida) 
