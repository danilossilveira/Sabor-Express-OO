from restaurante import Restaurante
from cardapio.bebiba import Bebida
from cardapio.comida import Comida

restaurante_1 = Restaurante('Churrascaria Silveira', 'Churrasco')
restaurante_1.alterar_estado()
restaurante_2 = Restaurante('Alemão', 'Pizzaria')
restaurante_3 = Restaurante('MD Lanches', 'Xis')

coca_cola = Bebida('Coca-Cola', 12, 'Grande')
coca_cola.aplicar_desconto()
alaminuta = Comida('Alaminuta', 25, 'A melhor alaminuta de POA')
churrasco = Comida('Churrasco',33,'Picanha e linguiça')
fanta_laranja = Bebida('Fanta laranja', 10, 'Grande')
restaurante_1.adicionar_no_cardapio(alaminuta)
restaurante_1.adicionar_no_cardapio(fanta_laranja)
restaurante_1.adicionar_no_cardapio(churrasco)
restaurante_1.adicionar_no_cardapio(coca_cola)
def main():
    restaurante_1.exibir_cardapio

if __name__ == '__main__':
    main()