#include <stdio.h>
#include <string.h>

void main(void){
    int age;
    char name[100], str[100];
    puts("Введите Ваше имя: ");
    scanf("%s", name);
    printf("Введите Ваш возраст: ");
    scanf("%i", &age);
    sprintf(str, "Здравствуйте %s.Ваш возраст %i лет", name, age);
    puts(str);
}