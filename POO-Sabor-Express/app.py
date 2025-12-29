class Restaurante:
    restaurantes = []
    def __init__ (self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f' Nome: {self.nome}\n Categoria: {self.categoria}\n Estado: {self.ativo}\n'

    def listar_restaurante():
        print('Nome'.ljust(20),'|Categoria'.ljust(22),'|Ativo')
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome.ljust(20)} | {restaurante.categoria.ljust(20)} | {restaurante.ativo}')

    


restaurante_1 = Restaurante('Rafa Sushi', 'Sushi')
restaurante_2 = Restaurante('Alemão', 'Pizzaria')
restaurante_3 = Restaurante('MD Lanches', 'Xis')

Restaurante.listar_restaurante()