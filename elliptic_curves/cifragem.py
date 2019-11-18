#!/usr/bin/env python

import random
from utils import readFile, writeFile


def calculateCurve(p, d, e):
    pass


def defineQ(curve):
    pass


def getPoints(plain_text):
    pass


def cipher(pm):
    pass


def main():
    p, d, e = 21, 1, 1
    curve = calculateCurve(p, d, e)
    writeFile("./curve.txt", curve)

    q = defineQ(curve)
    k = random()
    plain_text = readFile("./textos/texto-claro.txt")
    pm = getPoints(plain_text)

    cipher_text = cipher(pm)
    writeFile("./textos/texto-cifrado.txt", cipher_text)


main()
