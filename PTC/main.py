import logging
from serial import Serial
from Aplicacao import Aplicacao
from Codificador import Codificador
from Physic import Physic
import poller


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)  # DEBUG, INFO, WARNING, ERROR, CRITICAL

    app = Aplicacao()
    psc = Physic()

    psc.conecta(app)

    sched = poller.Poller()
    sched.adiciona(app)
    sched.despache()
