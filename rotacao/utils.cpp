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
}

int getRotorChar(int charIdx, int rotorPosition, std::string rotor) {
  int rotorIdx = (charIdx - 97) + rotorPosition;
  char rotorChar = rotor[rotorIdx%26];
#ifdef _DEBUG_
  printf("%c(%d)[%d]", charIdx, charIdx, charIdx-97);
  printf(" -> %c(%d)[%d]\n", rotorChar, rotorChar, rotorIdx);
#endif
  return rotorChar;
}
