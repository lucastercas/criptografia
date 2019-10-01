#include "cifrar.h"
#include "decifrar.h"
#include "util.h"

int main() {
  std::cout << "=== Cifra de Transposição - Linha x Coluna ===\n";

  std::string key;
  std::cout << "Digite a chave: ";
  cin >> key;

  std::string filePath;
  std::cout << "Digite o local do texto claro: ";
  cin >> filePath;
  std::string plainText = readFile(filePath);

  std::string cipheredText = cipher(plainText, key);

  std::string cipheredTextLocation = "textos/texto-cifrado.txt";
  writeFile(cipheredTextLocation, decipheredText);
  printf("Texto cifrado guardado em %s\n", cipheredTextLocation.s_str());

  std::string decipheredText = decipher(cipheredText, key);

  std::string decipheredTextLocation = "textos/texto-cifrado.txt";
  writeFile("textos/texto-decifrado.txt", decipheredText);
  printf("Texto decifrado guardado em %s\n", decipheredTextLocation.s_str());

  return 0;
}
