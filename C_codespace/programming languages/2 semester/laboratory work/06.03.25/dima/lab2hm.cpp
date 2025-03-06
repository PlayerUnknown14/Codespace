#include <fstream>
#include <iostream>
using namespace std;
int countNum(char*filename, int a, int b){
    ifstream fin;
    fin.open(filename, ios::in);
    if (!fin){
        cout<<"\n Нет исходного файла";
        return -1;
    }

    int count = 0;
    int number;
    while (fin>>number){
        if (number > a && number < b){
            count++;
        }
    }
    fin.close();
    return count;

}

int main(){
    int a = 10; 
    int b = 30;
    int result = countNum("C://Users//luvidmi//Desktop//git//Codespace//C_codespace//programming languages//2 semester//laboratory work//06.03.25//dima//numbers.txt1",a,b);
    if (result == -1){
        cout<<"Нет потоков";
    }
    else{
    cout<<"Количество чисел, больших "<<a<<", но меньших "<<b<<" = "<<result;
    }
    return 0;
}