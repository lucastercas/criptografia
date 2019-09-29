#include "cifrar.h"

/**
 */
std::string cipherTransposition(Matrix matrix, std::string key) {
  Matrix result;
  int lineIdx = 0;
  result.push_back(std::vector<char>());

  // Copia e ordenar a chave em ordem alfabetica
  std::string sortedKey = key;
  sort(sortedKey.begin(), sortedKey.end());
  /*
  std::cout << "=> Key: " << key << std::endl;
  std::cout << "=> Sorted Key: " << sortedKey << std::endl;
  */

  // Vetor pra saber se a posição atual da chave ja foi processada.
  // Isso é preciso por que pode ter letras repetidas na chave
  std::vector<bool> copied(key.size(), false);

  for (char c: sortedKey) {
    int index = key.find(c);
    while (copied[index]) {
      index = key.find(c, index+1);
    }
    //printf("=> Index(%c): %d\n", c, index);
    copied[index] = true;
    for (int i = 0; i < matrix.size(); i++) {
      result[lineIdx].push_back(matrix[i][index]);
    }
    lineIdx++;
    result.push_back(std::vector<char>());
  }
  //printMatrix(result);
  return matrixToText(result);
}

/**
 */
std::string cipher(std::string plainText, std::string key) {
  std::string noSpacePlainText = removeSpace(plainText);

  /* Primeiro Estagio */
  Matrix matrixStg1 = textToMatrix(noSpacePlainText, key.size());
  std::string cipherStg1 = cipherTransposition(matrixStg1, key);
  printf("\n=> Stage 1: %s\n", cipherStg1.c_str());

  /* Segundo Estagio */
  Matrix matrixStg2 = textToMatrix(cipherStg1, key.size());
  std::string cipherStg2 = cipherTransposition(matrixStg2, key);
  printf("\n=> Stage 2: %s\n", cipherStg2.c_str());

  /* Terceiro Estagio */
  Matrix matrixStg3 = textToMatrix(cipherStg2, key.size());
  std::string cipherStg3 = cipherTransposition(matrixStg3, key);
  printf("\n=> Stage 3: %s\n", cipherStg3.c_str());

  return cipherStg3;
}
