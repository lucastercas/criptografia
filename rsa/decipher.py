#!/usr/bin/env python

import random
from utils import readFile, writeFile


# Maior Divisor Comum de x e y
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


# Algoritmo Extendido de Euclide
# Calcula os coeficientes, tal que: ax + by = gcd(a, b)
def xgcd(a, b):
    x, x1 = 0, 1
    y, y1 = 1, 0

    if a == 0:
        return b, x, y

    while b != 0:
        quotient = a // b
        a, b = b, a - quotient * b
        x1, x = x, x1 - quotient * x
        y1, y = y, y1 - quotient * y

    return a, x1, y1


def isPrime(x):
    if x == 2:  # Se for 2, n é primo
        return True
    if x < 2 or x % 2 == 0:
        return False
    for n in range(3, int(x**0.5)+2, 2):
        if x % n == 0:
            return False
    return True


def calculateE(phi):
    while True:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
        if g == 1:
            return e


def calculateD(e, phi):
    g, x, y = xgcd(e, phi)
    if x < 0:
        return x + phi
    else:
        return x


def createKeys(p, q):
    if not (isPrime(p) and isPrime(q)):
        raise ValueError("P e Q devem ser primos")
    elif p == q:
        raise ValueError("P e Q não podem ser iguais")

    n = p * q
    phi = (p-1)*(q-1)

    e = calculateE(phi)

    d = calculateD(e, phi)

    return f"{e}\n{n}", f"{d}\n{n}"


def decipher(ciphertext):
    private_key_path = "./private-key.txt"
    with open(private_key_path) as file:
        key = file.readline()
        n = file.readline()
    lines = ciphertext.split("\n")
    n_lines = len(lines)
    deciphered = ""
    for i in range(n_lines-1):
        line = lines[i]
        aux = int(line) ** int(key)
        c = aux % int(n)
        deciphered += chr(c)

    return deciphered


def main():
    print("\n#===== Decifragem RSA =====#")

    option = None
    while True:
        print("1 - Gerar Chaves")
        print("2 - Decifrar Texto")
        option = input("Escolha: ")
        if (option == "1"):
            # Criar chaves publicas e privadas
            print("#=== Gerando Chaves ===#")
            public_key, private_key = createKeys(151, 139)

            writeFile("./public-key.txt", public_key)
            writeFile("./private-key.txt", private_key)
            break
        elif(option == "2"):
            cipher_text_path = "./textos/texto-cifrado.txt"
            cipher_text = readFile(cipher_text_path)
            deciphered_text = decipher(cipher_text)
            writeFile("./textos/texto-decifrado.txt", deciphered_text)
            break


main()
