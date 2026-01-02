class Restaurante:
    restaurantes = []
    def __init__ (self, nome, categoria):
        self._nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
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

restaurante_1 = Restaurante('Rafa Sushi', 'Sushi')
restaurante_1.alterar_estado()
restaurante_2 = Restaurante('Alemão', 'Pizzaria')
restaurante_3 = Restaurante('MD Lanches', 'Xis')

Restaurante.listar_restaurante()