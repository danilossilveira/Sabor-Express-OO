from veiculo import Veiculo
class Moto(Veiculo):
    def __init__(self, marca, modelo, cor, preco, cilindradas):
        super().__init__(marca, modelo, cor, preco)
        self._cilindradas = cilindradas

    def __str__(self):
        return (f'Marca: {self._marca}\nModelo: {self._modelo}\nCor: {self._cor}\nCilindradas: {self._cilindradas}\n')
    
    def exibir_veiculos(self):
        print(f'Marca: {self._marca}\nModelo: {self._modelo}\nCor: {self._cor}\nCilindradas: {self._cilindradas} \n')