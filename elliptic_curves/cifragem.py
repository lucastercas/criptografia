#!/usr/bin/env python

import random
import math

from utils import readFile, writeFile


def sumPoints(p1, p2, p, d):
    # p1 = (x1, y1) p2 = (x2, y2)
    # R = p1 + p2
    # xR = (λ^2 - x1 - x2) % p
    # yR = (λ(x1 - xR) - x1) % p
    lamb = calculateLambda(p1, p1, d)
    xr = (pow(lamb, 2) - p1[0] - p2[0]) % p
    yr = (lamb * (p1[0] - xr) - p1[1]) % p
    return (xr, yr)


def calculateLambda(p1, p2, d):
    if p1[0] == p2[0] and p1[1] == p2[1]:
        return (3 * pow(p1[0], 2) + d) / 2 * p1[1]
    else:
        return (p2[1] - p1[1]) / (p2[0] - p1[0])


def calculateQs(p, d, e):
    # y^2 % p = (x^3 + dx + e) % p
    # Descobrir X e Y
    curves = []
    for x in range(0, p):
        for y in range(0, p):
            left = pow(y, 2) % p
            right = (pow(x, 3) + d * x + e) % p
            if left == right:
                curves.append((x, y))
    return curves


def calculateSums(k, sums, decompositions, p, d):
    if k == 1:
        decompositions.append(1)
        return 1

    idx1 = idx2 = 1
    idx = idx1 + idx2
    if not idx in sums:
        sums[idx] = sumPoints(sums[idx1], sums[idx2], p, d)

    while idx <= math.ceil(k/2):
        idx1 = idx2 = idx
        idx = idx1 + idx2
        if not idx in sums:
            sums[idx] = sumPoints(sums[idx1], sums[idx2], p, d)
    decompositions.append(idx1)

    aux = k - idx1
    calculateSums(aux, sums, decompositions, p, d)


def defineQ(curve):
    pass


def getPoints(plain_text):
    pass


def cipher(pm):
    pass


def main():
    # Curva eliptica:
    p, d, e = 23, 1, 1

    # Calcular todos os pontos (x, y) possiveis
    qs = calculateQs(p, d, e)
    # Escolher um ponto (x, y) = q da curva
    q = qs[0]
    writeFile("./curve.txt", f"{q[0]}\n{q[1]}")

    # Escolher aleatoriamente K(chave privada)
    Ka = random.randint(0, 50)
    # Salvar a chave privada em um arquivo
    writeFile("keys/a_private_key.txt", f"{Ka}")

    # Calcular chave publica Ra (Ka * Q)
    sums = {} # Dicionario com as somas de q (multiplos de 2)
    sums[1] = q
    decompositions = [] # Vetor com Q decomposto em multiplos de 2
    calculateSums(Ka, sums, decompositions, p, d)
    
    public_key = sums[decompositions[0]]
    for i in range(1, len(decompositions)):
        public_key = sumPoints(public_key, sums[decompositions[i]], p, d)
    # Salvar a chave publica em um arquivo
    writeFile("keys/a_public_key.txt", f"{public_key[0]}\n{public_key[1]}")


    # plain_text = readFile("./textos/texto-claro.txt")
    # pm = getPoints(plain_text)

    # cipher_text = cipher(pm)
    # writeFile("./textos/texto-cifrado.txt", cipher_text)


main()
