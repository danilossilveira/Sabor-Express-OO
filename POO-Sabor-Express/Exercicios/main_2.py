from carro import Carro
from moto import Moto


onix = Carro('Chevrolet', 'Onix', 'Preto', 110000, 4)
honda_cg = Moto('Honda', 'CG', 'Cinza', 30000, 160)


def main():
    print(onix)
    print(honda_cg)
if __name__ == '__main__':
    main()