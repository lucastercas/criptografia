#!/usr/bin/env python

import sys
from cipher import cipher
from decipher import decipher


def readFile(file_path):
    # Caso o arquivo do texto claro n exista
    try:
        f = open(file_path, 'r')
        return f.read()
    except IOError:
        sys.exit()


def writeFile(file_path, content):
    f = open(file_path, 'w')
    f.write(content)


def main():
    print("\n#===== Transposição =====#")

    key = input("Digite a chave: ")

    # Numero de estagios do algoritmo
    n_stages = 3
    # Ler o texto claro
    plain_text_path = input("Digite o local do texto claro: ")
    plain_text = readFile(plain_text_path)

    # Cifrar o texto claro
    cipher_text = cipher(plain_text, key,  n_stages)

    # Salvar o texto cifrado
    cipher_text_path = plain_text_path.split('/')[:-1]
    cipher_text_path = '/'.join(cipher_text_path) + "/texto-cifrado.txt"
    writeFile(cipher_text_path, cipher_text)
    print(f"=> Texto cifrado salvo em {cipher_text_path}")

    # Decifrar o texto cifrado
    deciphered_text = decipher(cipher_text, key, n_stages)

    # Salvar o texto decifrado
    deciphered_text_path = plain_text_path.split('/')[:-1]
    deciphered_text_path = '/'.join(deciphered_text_path) + \
        "/texto-decifrado.txt"
    writeFile(deciphered_text_path, deciphered_text)
    print(f"=> Texto decifrado salvo em {deciphered_text_path}")


main()
