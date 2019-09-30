#include "cifrar.h"

int getRotorChar(int charIdx, int rotorPosition, std::string rotor) {
  int rotorIdx = charIdx + rotorPosition;
  char rotorChar = rotor[rotorIdx];
  return rotorChar;
}

std::string cipher(std::string plainText, std::vector<std::string> rotors) {
  // Inicializar a posição dos rotores aleatoriamente
  /*
  int leftRotorPosition = rand() % 26;
  int middleRotorPosition = rand() % 26;
  int rightRotorPosition = rand() % 26;
  */
  int leftRotorPosition = 6;
  int middleRotorPosition = 6;
  int rightRotorPosition = 6;

  // Salvar a posição inicial pra usar na decifragem
  int initialLeftRotorPosition = leftRotorPosition;
  int initialMiddleRotorPosition = middleRotorPosition;
  int initialRightRotorPosition = rightRotorPosition;

  for (char c: plainText) {
    char lowerCase = tolower(c);
    int charIdx = lowerCase - 97;
    int firstRotor = getRotorChar(charIdx, rightRotorPosition, rotors[0]);
    int secondRotor = getRotorChar(firstRotor, middleRotorPosition, rotors[1]);
  }

  return "iae";
}
