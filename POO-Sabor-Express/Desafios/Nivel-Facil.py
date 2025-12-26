class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)
      

    def __str__(self):
        return (f' Nome: {self.nome}\n Categoria: {self.categoria} \n Estatus: {self.ativo}')
    
    def listar_restaurantes():
         for restaurante in Restaurante.restaurantes:
              print(f' Nome: {restaurante.nome} \n Categoria: {restaurante.categoria} \n Estatus: {restaurante.ativo}')



    def ativar_restaurante():
        buscar_restaurante = input('Quer ativar qual restaurante?')
        for restaurante in Restaurante.restaurantes:
            if buscar_restaurante == restaurante:
                restaurante.ativo = not restaurante.ativo
                print('Restaurante Ativado com sucesso')
                  

Restaurante.ativar_restaurante()
Restaurante.listar_restaurantes()  





restaurante_1 = Restaurante('Bento açaí', 'Açaiteria')
restaurante_2 = Restaurante('MD Lanches', 'Hamburgueria')
restaurante_3 = Restaurante('Alemão', 'Pizzaria')  