from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Anderson', 10)
restaurante_praca.receber_avaliacao('Tamara', 8)
restaurante_praca.receber_avaliacao('Arthur', 5)

def main():
  Restaurante.listar_restaurantes()

if __name__ == '__main__':
  main()