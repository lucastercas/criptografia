#include "utils.h"
#include "cifrar.h"
#include "decifrar.h"

int main() {
  printf("=== Maquina de Rotação ===");

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

  return 0;
}
