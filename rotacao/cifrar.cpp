#include "cifrar.h"

std::string cipher(std::string plainText, std::vector<std::string> rotors, std::vector<int> rotorPositions) {
  std::string cipherText = "";

  for (char c: plainText) {
    char lowerCase = tolower(c);
  int rightRotorPosition = rotorPositions[0];
  int middleRotorPosition = rotorPositions[1];
  int leftRotorPosition = rotorPositions[2];

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
