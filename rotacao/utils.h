#ifndef UTILS_H
#define UTILS_H
#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <ctime>

void writeFile(std::string filePath, std::string content);
std::string readFile(std::string filePath);

#endif
