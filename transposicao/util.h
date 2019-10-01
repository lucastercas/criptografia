#ifndef UTIL_H
#define UTIL_H

#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <algorithm>
#include <cstdio>

typedef std::vector<std::vector<char> > Matrix;

std::string removeSpace(std::string);
void printMatrix(Matrix);
Matrix textToMatrix(std::string, int);
std::string matrixToText(Matrix);
bool writeFile(std::string, std::string);
std::string readFile(std::string);

#endif
