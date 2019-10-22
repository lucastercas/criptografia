#include "cifrar.h"
#include "decifrar.h"
#include "util.h"

int main() {
  std::cout << "=== Cifra de Transposição - Linha x Coluna ===\n";

  std::string key;
  std::cout << "Digite a chave: ";
  std::cin >> key;

  /* Ler e guardar o texto claro */
  std::string filePath;
  std::cout << "Digite o local do texto claro: ";
  std::cin >> filePath;
  std::string plainText = readFile(filePath);

  /* Texto cifrado */
  std::string cipherText = cipher(plainText, key);
  std::string cipherTextLocation = "textos/texto_cifrado.txt";
  writeFile(cipherTextLocation, cipherText);
  printf("Texto cifrado guardado em %s\n", cipherTextLocation.c_str());

  /* Texto decifrado */
  std::string decipheredText = decipher(cipherText, key);
  std::string decipheredTextLocation = "textos/texto_decifrado.txt";
  writeFile(decipheredTextLocation, decipheredText);
  printf("Texto decifrado guardado em %s\n", decipheredTextLocation.c_str());

  return 0;
}
