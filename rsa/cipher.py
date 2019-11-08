#!/usr/bin/env python

import sys
from utils import readFile, writeFile


def cipher(plaintext):
    public_key_path = "./public-key.txt"
    with open(public_key_path) as file:
        key = file.readline()
        n = file.readline()

    cipher_text = ""
    for char in plaintext:
        k = ord(char)
        k = k ** int(key)
        d = k % int(n)
        cipher_text += f"{d}\n"

    return cipher_text


def main():
    print("#===== Cifragem RSA =====#")

    plain_text_path = input("Caminho do texto claro: ")
    plain_text = readFile(plain_text_path)
    cipher_text = cipher(plain_text)
    print(f"Texto cifrado escrito para ./textos/texto-cifrado.txt")
    writeFile("./textos/texto-cifrado.txt", cipher_text)


main()
