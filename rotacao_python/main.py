#!/usr/bin/env python
import copy

from cipher import cipher
from decipher import decipher

_DEBUG_ = True


def readFile(file_path):
    f = open(file_path, 'r')
    return f.read()


def save_file(file_path, content):
    f = open(file_path, 'w')
    return f.write(content)


def main():
    print("\n#===== Maquina de Rotação =====#")

    rotors = [
        "ekmflgdqvzntowyhxuspaibrcj",
        "ajdksiruxblhwtmcqgznpyfvoe",
        "bdfhjlcprtxvznyeiwgakmusqo",
    ]

    rotors_position = [3, 10, 4]

    # Ler o texto claro
    plain_text_path = "./textos/texto-claro.txt"
    plain_text = readFile(plain_text_path)
    print(f"==> Plain Text: {plain_text}")

    # Cifrar o texto claro
    cipher_text = cipher(plain_text, rotors, copy.copy(rotors_position))
    print(f"==> Cipher Text: {cipher_text}")

    # Salvar o texto cifrado
    cipher_text_path = "./textos/texto-cifrado.txt"
    save_file(cipher_text_path, cipher_text)

    # Decifrar o texto cifrado
    deciphered_text = decipher(cipher_text, rotors, copy.copy(rotors_position))
    print(f"==> Deciphered Text: {deciphered_text}")

    # Salvar o texto decifrado
    deciphered_text_path = "./textos/texto-decifrado.txt"
    save_file(deciphered_text_path, deciphered_text)


main()
