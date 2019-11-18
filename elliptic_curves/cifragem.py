#!/usr/bin/env python

import random
from utils import readFile, writeFile

def sumPoints(p1, p2, p):
  # p1 = (x1, y1) p2 = (x2, y2)
  # R = p1 + p2
  # xR = (λ^2 - x1 - x2) % p
  # yR = (λ(x1 - xR) - x1) % p
  pass

def calculateLambda(p1, p2):
  pass

def calculateCurve(p, d, e):
    # y^2 % p = (x^3 + dx + e) % p
    # Descobrir X e Y
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
