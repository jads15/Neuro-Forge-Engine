from abc import ABC, abstractmethod
class TransformadorDados(ABC):
    def __init__(self):
     pass
    @abstractmethod
    def fit(self,dados):
        pass

    @abstractmethod
    def transform(self,dados):
        pass

class  MinMaxScaler(TransformadorDados):
    def __init__(self):
          super().__init__()
          self.xmin = None
          self.xmax  =None

    def fit(self,dados):
         self.xmin = min(dados)
         self.xmax = max(dados)

    def transform(self, dados):
       
       dados_normalizados = []
       for valor in dados:
          normalizacao = (valor-self.xmin)/(self.xmax -self.xmin)
          dados_normalizados.append(normalizacao)     
       return dados_normalizados

class LabelCategoricalEncoder(TransformadorDados):
    def __init__(self):
        super().__init__()

    def fit(self, categorias):
        categorias_nao_repetidas = set(categorias)
        categorias_lista = list(categorias)
        categorias_ordenada = categorias_lista.sort()
        dict_categorias = {i: valor for i, valor in enumerate(categorias_ordenada) }
        return dict_categorias

    def transform(self, dados):
        valores = [] 
        for valor, chave in dados:
            valores.append(valor)
        return valores    