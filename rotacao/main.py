#!/usr/bin/env python
import copy
import random
import sys

from cipher import cipher
from decipher import decipher

def readFile(file_path):
    try:
        f = open(file_path, 'r')
        return f.read()
    except IOError:
        print(f"Arquivo {file_path} não existe")
        sys.exit()


def save_file(file_path, content):
    f = open(file_path, 'w')
    return f.write(content)


def main():
    print("\n#===== Maquina de Rotação =====#")

    # Rotores que serão usados
    rotors = [
        "ekmflgdqvzntowyhxuspaibrcj",
        "ajdksiruxblhwtmcqgznpyfvoe",
        "bdfhjlcprtxvznyeiwgakmusqo",
    ]

    # Posição inicial dos rotores
    rotors_position = [
        random.randint(0, 25),
        random.randint(0, 25),
        random.randint(0, 25)
    ]

    # Ler o texto claro
    plain_text_path = input("Digite o local do textoc claro: ")
    plain_text = readFile(plain_text_path)

    # Cifrar o texto claro
    cipher_text = cipher(plain_text, rotors, copy.copy(rotors_position))

    # Salvar o texto cifrado
    cipher_text_path = plain_text_path.split('/')[:-1]
    cipher_text_path = '/'.join(cipher_text_path) + "/texto-cifrado.txt"
    save_file(cipher_text_path, cipher_text)
    print(f"=> Texto cifrado salvo em {cipher_text_path}")

    # Decifrar o texto cifrado
    deciphered_text = decipher(cipher_text, rotors, copy.copy(rotors_position))
    
    # Salvar o texto decifrado
    deciphered_text_path = plain_text_path.split('/')[:-1]
    deciphered_text_path = '/'.join(deciphered_text_path) + \
        "/texto-decifrado.txt"
    save_file(deciphered_text_path, deciphered_text)
    print(f"=> Texto decifrado salvo em {deciphered_text_path}")


main()
