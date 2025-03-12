#include <iostream>
#include <fstream>
#include <locale>
int gen(char* names, char* words){
    std::ifstream finName;
    finName.open("names.txt", std::ios::in);
    if (!finName){
        std::cout<<"Файл 'names.txt' не существует";
        return -1;
    }
    std::ifstream finWord;
    finWord.open(words, std::ios::in);
    if (!finWord){
        std::cout<<"Файл 'names.txt' не существует";
        return -1;
    }
    char name;
    int size;
    finName >> size;
    char** nameMass = new char*[size];
    for(int i = 0; i<size; i++){
        nameMass[i] = new char[size];
    }
    for (int i = 0; i<size; i++){
        finName >> nameMass[i];
    }
    for (int i=0; i<size; i++){
        std::cout<<nameMass[i];
    }
    return 0;
}
