import sys
from Subcamada import Subcamada
from Quadro import Quadro
import logging  # https://realpython.com/python-logging/
from serial import Serial

class Aplicacao(Subcamada):

    def __init__(self, serial_port):
        # Subcamada.__init__(self, sys.stdin, 3)
        Subcamada.__init__(self, serial_port, 3)
        self.disable_timeout()
        logging.basicConfig(level=logging.WARNING)  # DEBUG, INFO, WARNING, ERROR, CRITICAL
        self.serial_port = serial_port

    def recebe(self, quadro):
        logging.info('App.recebe(): Chegou aqui')
        print('> ' + quadro.dados.decode('ascii'))

    def handle(self):
        b = self.serial_port.read(1)
        print(b)
        # msg = sys.stdin.readline()[:-1]
        # dados = msg.encode('ascii')
        # logging.info('App.handle: ' + msg)
        # logging.info('App.handle: dados.ecode(ascii) abaixo:')
        # logging.info(dados)

        # while len(dados) > 0:
        #     quadro = Quadro()
        #     quadro.data = dados[0:128]
        #     logging.info('App.handle: ' + quadro.data.decode('ascii'))
        #     self.lower.envia(quadro)
        #     dados = dados[1024:]
