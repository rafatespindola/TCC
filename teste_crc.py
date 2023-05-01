#!/usr/bin/python3
import binascii
import crc_ifsc as crc_ifsc

fcs = crc_ifsc.CRC16(b'bom')

msg = fcs.gen_crc()
print('Mensagem com FCS:', msg)

som  = msg.hex()

print('Dehex(): ' + str(binascii.unhexlify(som)))

for i in som:
    print(i)

fcs.clear()
fcs.update(msg)
print('Resultado da verificação da mensagem com FCS:', fcs.check_crc())

msg=msg[:-1]
fcs.clear()
fcs.update(msg)
print('Resultado da verificação da mensagem com FCS após modificá-la:', fcs.check_crc())



