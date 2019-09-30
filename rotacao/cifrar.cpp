#include "cifrar.h"

int getRotorChar(int charIdx, int rotorPosition, std::string rotor) {
  int rotorIdx = (charIdx - 97) + rotorPosition;
  char rotorChar = rotor[rotorIdx%26];
#ifdef _DEBUG_
  printf("%c(%d)[%d]", charIdx, charIdx, charIdx-97);
  printf(" -> %c(%d)[%d]\n", rotorChar, rotorChar, rotorIdx);
#endif
  return rotorChar;
}

std::string cipher(std::string plainText, std::vector<std::string> rotors) {
  std::string cipherText = "";
  /*
  int leftRotorPosition = rand() % 26;
  int middleRotorPosition = rand() % 26;
  int rightRotorPosition = rand() % 26;
  */

  // Inicializar a posição dos rotores aleatoriamente e salvar a posição inicial
  // deles pra usar na decifragem
  int rightRotorPosition = 3;
  int initialRightRotorPosition = rightRotorPosition;

  int middleRotorPosition = 3;
  int initialMiddleRotorPosition = middleRotorPosition;

  int leftRotorPosition = 3;
  int initialLeftRotorPosition = leftRotorPosition;

  for (char c: plainText) {
    char lowerCase = tolower(c);

#ifdef _DEBUG_
    printf("Primeiro Rotor: ");
#endif
    int firstRotorOutput = getRotorChar(lowerCase, rightRotorPosition, rotors[0]);
    // Girar o primeiro rotor
    rightRotorPosition =  (rightRotorPosition + 1) % 26;

    // Se o primeiro rotor fez uma volta completa, rodar o segundo rotor
    if (rightRotorPosition == 0) middleRotorPosition = (middleRotorPosition + 1) % 26;
#ifdef _DEBUG_
    printf("Segundo Rotor: ");
#endif
    int secondRotorOutput = getRotorChar(firstRotorOutput, middleRotorPosition, rotors[1]);

    // Se o segundo rotor fez uma volta completa, rodar o terceiro rotor
    if (middleRotorPosition == 0) leftRotorPosition = (leftRotorPosition + 1) % 26;
#ifdef _DEBUG_
    printf("Terceiro Rotor: ");
#endif
    int thirdRotorOutput = getRotorChar(secondRotorOutput, leftRotorPosition, rotors[2]);
    cipherText += thirdRotorOutput;
  }

  return cipherText;
}
