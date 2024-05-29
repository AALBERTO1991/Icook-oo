from modelos.avaliacao import Avaliacao

class Restaurante:
    '''Essa classe representa um restaurante e suas caracteristicas'''
    resturantes = []
    
    '''Essa função iniciliza uma instancia da classe Restaurante.
    
    Parâmetros:
    - nome(str): nome do Restaurante
    - categoria (str): A categoria do Restaurante
    '''
    def __init__(self, nome, categoria):
      self._nome = nome.title()
      self._categoria = categoria.upper()
      self._ativo = False
      self._avaliacao = []
      Restaurante.resturantes.append(self)
    
    '''Essa função retorna em string uma representação do restaurante cadastrado'''
    def __str__(self) -> str:
      return f'{self._nome} | {self._categoria}'
    
    '''Essa função classmethod Exibe uma lista formatada de todos os restaurantes cadastrados
    o parametro .ljust(25) foi utilizado para carrigir a visão do código no terminal
    '''
    @classmethod
    def listar_restaurantes(cls):
      print (f'\n{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | Status')
      print('-------------------------------------------------------------------------------------')
      for restaurante in cls.resturantes:
        print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)}| {restaurante.ativo}')
      print()

    '''Retorna um símbolo indicando o estado de atividade do restaurante.'''
    @property
    def ativo(self):
      return '✔️' if self._ativo else '❌'
    
    '''Alterna o estado de atividade do restaurante.'''
    def alternar_estado(self):
      self._ativo = not self._ativo
    
    '''
    Registra uma avaliação para o restaurante.

    Parâmetros:
    - cliente (str): O nome do cliente que fez a avaliação.
    - nota (float): A nota atribuída ao restaurante (entre 1 e 5).
    '''
    def receber_avaliacao(self, cliente, nota):
      if 0 < nota <= 5:
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)
    
    '''Calcula e retorna a média das avaliações do restaurante.'''
    @property
    def media_avaliacoes(self):
      if not self._avaliacao:
        return '-'
      soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
      quantidade_de_notas = len(self._avaliacao)
      media = round(soma_das_notas / quantidade_de_notas, 1)
      return media