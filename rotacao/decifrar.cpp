#include "utils.h"
#include "decifrar.h"

std::string decipher(std::string cipherText, std::vector<std::string> rotors, std::vector<int> rotorPositions) {
  std::string decipherText = "";

  int rightRotorPosition = rotorPositions[0];
  int middleRotorPosition = rotorPositions[1];
  int leftRotorPosition = rotorPositions[2];

  for (char c: cipherText) {
    int firstRotorOutput = getRotorChar(c, rightRotorPosition, rotors[0]);
    rightRotorPosition =  (rightRotorPosition + 1) % 26;

    if (rightRotorPosition == 0) middleRotorPosition = (middleRotorPosition + 1) % 26;
    int secondRotorOutput = getRotorChar(firstRotorOutput, middleRotorPosition, rotors[1]);

    if (middleRotorPosition == 0) leftRotorPosition = (leftRotorPosition + 1) % 26;
    int thirdRotorOutput = getRotorChar(secondRotorOutput, leftRotorPosition, rotors[2]);

    decipherText += thirdRotorOutput;
  }

  return decipherText;
}
