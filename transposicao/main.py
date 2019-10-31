#!/usr/bin/env python

import argparse

from cipher import cipher
from decipher import decipher


def readFile(file_path):
    f = open(file_path, 'r')
    return f.read()


def writeFile(file_path, content):
    f = open(file_path, 'w')
    f.write(content)


def main():
    print("\n#===== Transposição =====#")

    # parser = argparse.ArgumentParser(description='Cifra de Transposição')
    # parser.add_argument('')

    key = "loucura"
    plain_text_path = "./textos/texto-claro.txt"
    plain_text = readFile(plain_text_path)
    cipher_text = cipher(plain_text, key)

    cipher_text_path = "./textos/texto-cifrado.txt"
    writeFile(cipher_text_path, cipher_text)

    deciphered_text = decipher(cipher_text, key)
    deciphered_text_path = "./textos/texto-decifrado.txt"
    writeFile(deciphered_text_path, deciphered_text)


main()
