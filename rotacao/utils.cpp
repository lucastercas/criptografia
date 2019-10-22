#include "utils.h"

std::string readFile(std::string filePath) {
  std::ifstream file;
  file.open(filePath);

  std::string content;
  std::string line;
  if (file.is_open()) {
    while (getline(file, line)) {
      content += line;
    }
    file.close();
  }
  return content;
}

void writeFile(std::string filePath, std::string content) {
  std::ofstream file;
  file.open(filePath);
  file << content;
  file.close();
}

int getRotorChar(int charIdx, int rotorPosition, std::string rotor) {
  int rotorIdx = (charIdx - 97) + rotorPosition;
  char rotorChar = rotor[rotorIdx%26];
  return rotorChar;
}
