#include "cifrar.h"
#include "decifrar.h"
#include "util.h"

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

int main() {
  std::cout << "=== Cifra de Transposição - Linha x Coluna ===\n";

  std::string key;
  std::cout << "Digite a chave: ";
  key = "lucasde";
  //cin >> key;

  std::string filePath;
  std::cout << "Digite o local do texto claro: ";
  filePath = "output/texto_claro.txt";
  //cin >> filePath;
  std::string plainText = readFile(filePath);

  std::string cipheredText = cipher(plainText, key);
  std::cout << cipheredText;

  std::string decipheredText = decipher(cipheredText, key);
  std::cout << decipheredText;

  return 0;
}
