import sys
from Subcamada import Subcamada
from Quadro import Quadro

class Aplicacao(Subcamada):

    def __init__(self):
        Subcamada.__init__(self, sys.stdin, 3)
        self.disable_timeout()

    def recebe(self, quadro):
        print('> ' + quadro.dados.decode('ascii'))

    def handle(self):
        msg = sys.stdin.readline()[:-1]
        dados = msg.encode('ascii')

        while len(dados) > 0:
            quadro = Quadro()
            quadro.data = dados[0:32]
            self.lower.envia(quadro)
            dados = dados[32:]
