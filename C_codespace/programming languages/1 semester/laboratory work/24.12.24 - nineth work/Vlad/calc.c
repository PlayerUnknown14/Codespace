#include <stdio.h>
#include <stdlib.h>
#include <string.h>

double calculate(double num1, double num2, char operator) {
    switch (operator) {
        case '+':
            return num1 + num2;
        case '-':
            return num1 - num2;
        case '*':
            return num1 * num2;
        case '/':
            return num1 / num2;
    }
}

int main(int argc, char *argv[], char *envp[]){
    double num1 = 0, num2 = 0;
    char operator;

    num1 = atof(argv[1]);
    num2 = atof(argv[3]);
    operator = argv[2][0];
    
    for (int i = 0; i < argc; i++)
        printf("%s\n", argv[i]);

    double result = calculate(num1, num2, operator);

    printf(" = %f\n", result);

}