from veiculo import Veiculo
class Carro(Veiculo):
    def __init__(self, marca, modelo, cor, preco, portas):
        super().__init__(marca, modelo, cor, preco)
        self._portas = portas

    def __str__(self):
        return (f'Marca: {self._marca}\nModelo: {self._modelo}\nCor: {self._cor}\n{self._portas} Portas\n')

    def exibir_veiculos(self):
        print(f'Marca: {self._marca}\nModelo: {self._modelo}\nCor: {self._cor}\n{self._portas} Portas\n')