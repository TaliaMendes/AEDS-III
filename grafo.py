class Grafo:

  def __init__(self):
    self.numero_de_no = 0
    self.numero_de_aresta = 0
    self.grafo = {}

  def CriandoNo(self, no):
    if no not in self.grafo:
      self.grafo[no] = {}
      self.numero_de_no += 1

  def CriandoVizinhos(self, no, vizinho, peso):
    if no not in self.grafo:
      self.CriandoNo(no)
    if vizinho not in self.grafo:     #se nao tiver o no que faz ligação tem que criar, pois precisa dele para fazer ligação kkk
      self.CriandoNo(vizinho)

    self.grafo[no][vizinho] = peso
    self.numero_de_aresta += 1