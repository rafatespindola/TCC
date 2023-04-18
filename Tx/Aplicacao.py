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
        quadro = Quadro()
        info = sys.stdin.readline()[:-1]
        quadro.data = info.encode('ascii') 
        self.lower.envia(quadro)

