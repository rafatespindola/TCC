import logging
from serial import Serial
from Aplicacao import Aplicacao
from Codificador import Codificador
from Physic import Transmissor
import poller
import sys


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)  # DEBUG, INFO, WARNING, ERROR, CRITICAL

    app = Aplicacao()
    cod = Codificador()
    tms = Transmissor()

    cod.conecta(app)
    tms.conecta(cod)

    sched = poller.Poller()
    sched.adiciona(app)
    sched.despache()
