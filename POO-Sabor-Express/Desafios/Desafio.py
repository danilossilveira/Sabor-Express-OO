import os
class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)
        
    def __str__(self):
        return (f' Nome: {self.nome}\n Categoria: {self.categoria} \n Estados: {self.ativo}')
    
    def voltar_menu():
        input('Enter para voltar ao menu')
        os.system('cls')
        Restaurante.escolhas()
    
    def listar_restaurantes():
         for restaurante in Restaurante.restaurantes:
              print(f' Nome: {restaurante.nome} \n Categoria: {restaurante.categoria} \n Estatus: {restaurante.ativo}\n')
         Restaurante.voltar_menu()

    def ativar_restaurante():
        buscar_restaurante = input('Quer ativar qual restaurante?\n')
        for restaurante in Restaurante.restaurantes:
            if buscar_restaurante == restaurante.nome and restaurante.ativo == True:
                print(f'Este restaurante já está ativado')
                break 
            else:    
                if buscar_restaurante == restaurante.nome:
                    restaurante.ativo = not restaurante.ativo
                    print('Restaurante Ativado com sucesso')
                    break
        else:
            print('Restaurante não cadastrado')
        Restaurante.voltar_menu() 

    def desativar_restaurante():
        buscar_restaurante = input('Quer desativar qual restaurante?\n')
        for restaurante in Restaurante.restaurantes:
            if buscar_restaurante == restaurante.nome and restaurante.ativo == False:                           
                print('Esse restaurante já está desativado')
                break                    
            else:
                if buscar_restaurante == restaurante.nome:
                    restaurante.ativo = not restaurante.ativo
                    print('Restaurante Desativado com sucesso com sucesso')
                    break
        else:
            print('Restaurante não cadastrado')    
        Restaurante.voltar_menu() 
       
    def listar_restaurantes_ativos():
        for restaurante in Restaurante.restaurantes:
            if restaurante.ativo == True:            
                print(restaurante,'\n')
        else:
            print('Não tem nenhum restaurante ativo')
           
        Restaurante.voltar_menu()
               
    def listar_restaurantes_desativados():
        for restaurante in Restaurante.restaurantes:
            if restaurante.ativo == False:
                print(restaurante,'\n') 
        else:
            print('Não tem nenhum restaurante desativado no momento')
                
        Restaurante.voltar_menu() 

    def escolhas():
     try:    
        escolha = int(input('''
        1- Ativar restaurante
        2- Desativar restaurante
        3- Listar todo os restaurantes
        4- Listar restaurantes ativos
        5- Listar restaurantes desativados
        6- Sair \n                                                                                                                     
        '''))
        match escolha:
            case 1:
                Restaurante.ativar_restaurante()
            case 2: 
                Restaurante.desativar_restaurante()
            case 3:
                Restaurante.listar_restaurantes()
            case 4:
                Restaurante.listar_restaurantes_ativos()
            case 5:
                Restaurante.listar_restaurantes_desativados()
            case 6:
                print('Até mais...')    
            case _:
                print('Opção inválida')
                Restaurante.voltar_menu() 
     except(ValueError):  
        print('Você só pode por números')
        Restaurante.voltar_menu()      



restaurante_1 = Restaurante('Bento açaí', 'Açaiteria')
restaurante_2 = Restaurante('MD Lanches', 'Hamburgueria')
restaurante_3 = Restaurante('Alemão', 'Pizzaria')

def main():
    Restaurante.escolhas()

if __name__ == '__main__':
    Restaurante.escolhas()    
