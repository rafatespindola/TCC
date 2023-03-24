from enum import Enum


class Estado(Enum):
  Q0=0
  Q1=1
  Q2=2

class Physical:

  def __init__(self):
    # aqui se armazena o estado atual
    self.estado = Estado.Q0
    # e esta é a tabela de handlers, feita com um dicionário
    self._handlers = {Estado.Q0: self.handle_q0, Estado.Q1: self.handle_q1, 
                      Estado.Q2: self.handle_q2}

  def mef(self, evento):
    # a escolha do handler fica muito mais simples !
    # basta indexar a tabela com o valor do estado atual, obtendo assim o respectivo handler
    # aí é só executá-lo
    self._handlers[self.estado](evento)

  def handle_q0(self, evento):
    # tratador de eventos no estado Q0
    self.estado = Estado.Q1

  def handle_q1(self, evento):
    # tratador de eventos no estado Q1
    self.estado = Estado.Q2

  def handle_q2(self, evento):
    # tratador de eventos no estado Q2
    self.estado = Estado.Q0