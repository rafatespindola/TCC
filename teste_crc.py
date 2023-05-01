#!/usr/bin/python3
import binascii
import crc_ifsc as crc_ifsc

fcs = crc_ifsc.CRC16(b'rafatespindola')

msg = fcs.gen_crc()
print('Mensagem com FCS:', msg)
print('tamanhp: ' + str(len(msg)))
som  = msg.hex()

print('Dehex(): ' + str(binascii.unhexlify(som)))

fcs.clear()
fcs.update(msg)
print('Resultado da verificação da mensagem com FCS:', fcs.check_crc())



