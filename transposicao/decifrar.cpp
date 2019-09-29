#include "decifrar.h"

std::string decipherTransposition(Matrix matrix, std::string key) {
  std::string sortedKey = key;
  sort(sortedKey.begin(), sortedKey.end());
  std::string result = "";

  // printf("Size: %d\n", matrix[0].size());

  for (int i = 0; i < matrix[0].size(); i++) {
    std::vector<bool> copied(key.size(), false);
    // printf("=> I: %d\n", i);
    for (char c: key) {
      int index = sortedKey.find(c);
      while (copied[index]) {
        int nextIndex = key.find(c, index+1);
        if (nextIndex < 0) break;
        index = nextIndex;
      } 
      copied[index] = true;
      result += matrix[index][i];
      // printf("-> Char: %c, Index: %d => %c\n", c, index, matrix[index][i]);

    }
  }
  return result;

}

std::string decipher(std::string cipherText, std::string key) {

  Matrix matrixStg1 = textToMatrix(cipherText, (int) cipherText.size() / key.size());
  std::string textStg1 = decipherTransposition(matrixStg1, key);
  printf("\n=> Stage 1: %s\n", textStg1.c_str());
  
  Matrix matrixStg2 = textToMatrix(textStg1, (int) cipherText.size() / key.size());
  std::string textStg2 = decipherTransposition(matrixStg2, key);
  printf("\n=> Stage 2: %s\n", textStg2.c_str());

  Matrix matrixStg3 = textToMatrix(textStg2, (int) cipherText.size() / key.size());
  std::string textStg3 = decipherTransposition(matrixStg3, key);
  printf("\n=> Stage 3: %s\n", textStg3.c_str());
  
  return textStg3;
}
