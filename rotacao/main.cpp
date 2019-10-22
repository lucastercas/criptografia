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
  std::vector<int> rotorPositions;
  rotorPositions.push_back(rand()%26); // Rotor direito 
  rotorPositions.push_back(rand()%26); // Rotor do meio
  rotorPositions.push_back(rand()%26); // Rotor esquerdo

  /* Ler e guardar o texto claro */
  std::string filePath;
  std::cout << "Local do Texto Claro: ";
  std::cin >> filePath;
  std::string plainText = readFile(filePath);

  /* Texto cifrado */
  std::string cipherText = cipher(plainText, rotors, rotorPositions);
  std::string cipherTextLocation = "textos/texto_cifrado.txt";
  writeFile(cipherTextLocation, cipherText);
  printf("Texto cifrado guardado em %s\n", cipherTextLocation.c_str());

  /* Texto decifrado */
  std::string decipheredText = decipher(cipherText, rotors, rotorPositions);
  std::string decipheredTextLocation = "textos/texto_decifrado.txt";
  writeFile("textos/texto-decifrado.txt", decipheredText);
  printf("Texto decifrado guardado em %s\n", decipheredTextLocation.c_str());

  return 0;
}
