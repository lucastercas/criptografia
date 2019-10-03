#include "util.h"

/* Recebe uma string e retorn a string sem espaços */
std::string removeSpace(std::string plainText) {
  std::string result = "";

  for (char c: plainText) {
    if (c != ' ') result += c;
  }
  return result;
}

/* Função pra imprimir uma matriz */
void printMatrix(Matrix matrix) {
  printf("\n=== Imprimindo Matriz ===\n");
  for (int i = 0; i < matrix.size(); i++) {
    for (int j = 0; j < matrix[i].size(); j++) {
      std::cout << matrix[i][j];
    }
    printf("\n");
  }
  printf("\n");
}

/**
 * Transforma uma string em uma matriz com 
 * {nCol} colunas e {text.size() / nCol} linhas
 */
Matrix textToMatrix(std::string text, int nCol) {
  Matrix matrix;
  int line = 0;
  int i;

  // Transformar o texto claro para forma de matrix
  matrix.push_back(std::vector<char>());
  for (i = 0; i < text.size(); i++) {
    if ((i % nCol == 0) && i != 0) {
      line++;
      matrix.push_back(std::vector<char>());
    }
    matrix[line].push_back(text[i]);
  }

  // Adicionar letras se faltar na ultima linha
  while (i % nCol != 0) {
    matrix[line].push_back('x');
    i++;
  }

  return matrix;
}

/**
 * Transforma uma matriz de chars em string
 */
std::string matrixToText(Matrix matrix) {
  std::string text = "";
  for (int i = 0; i < matrix.size(); i++) {
    for (int j = 0; j < matrix[i].size(); j++) {
      text += matrix[i][j];
    }
  }
  return text;
}

/**
 * Retorna o conteudo do arquivo em filepath
 */
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

/**
 * Escreve {content} no arquivo em {filePath}
 */
bool writeFile(std::string filePath, std::string content) {
  return true;
}
