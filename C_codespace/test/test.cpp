#include <iostream>

int mass[3][3];

int main(){
    for(int i=0; i<3; i++){
        for(int j=0; j<3; j++)
            std::cin>>mass[i][j];
}
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++)
            std::cout << mass[i][j] << " ";
        std::cout << std::endl;
}
return 0;
}