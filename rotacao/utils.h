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

//#define _DEBUG_ 0

void writeFile(std::string, std::string);
std::string readFile(std::string);
int getRotorChar(int, int, std::string);

#endif
