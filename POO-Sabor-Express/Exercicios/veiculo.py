from abc import ABC,abstractmethod
class Veiculo:
    def __init__(self, marca, modelo, cor, preco):
        self._marca = marca
        self._modelo = modelo
        self._cor = cor
        self._preco = preco

    @abstractmethod
    def exibir_veiculos(self):
        pass