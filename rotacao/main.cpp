#include "utils.h"
#include "cifrar.h"
#include "decifrar.h"

int main() {
  printf("\n=== Maquina de Rotação ===\n");

  // Inicializar os rotores
  std::vector<std::string> rotors = {
    "ekmflgdqvzntowyhxuspaibrcj", // Primeiro Rotor (direita)
    "ajdksiruxblhwtmcqgznpyfvoe", // Segundo Rotor (meio)
    "bdfhjlcprtxvznyeiwgakmusqo"  // Terceiro Rotor (esquerda)
  };

  // Inicializar semente do random
  srand(time(NULL));

  std::string filePath;
  std::cout << "Local do Texto Claro: ";
  filePath = "./textos/texto-claro.txt";
  //std::cin >> filePath;
  std::string plainText = readFile(filePath);
  std::cout << plainText << std::endl;

  std::string cipherText = cipher(plainText, rotors);
  printf("Plain Text: %s\n", plainText.c_str());
  printf("Cipher Text: %s\n", cipherText.c_str());

  return 0;
}
