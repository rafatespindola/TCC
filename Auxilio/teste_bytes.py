frase = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM123456789'

# Printar com tipo string o valor de 'frase' em hexa
print(frase.encode('ascii').hex())

# Transmitiu em hexa pelo som

# Printar frase original
recebido = '4f6c61206d756e646f'
print(bytes.fromhex(recebido).decode('ascii'))
