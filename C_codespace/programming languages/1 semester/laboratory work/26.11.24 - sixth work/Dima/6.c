#include <stdio.h>
#include <string.h>
 void main(){
    int length = 0;
    char word[100];
    printf("Введите слово: ");
    scanf("%s", word);
    length = strlen(word)/2;
    if (strlen(word)%2 == 0){
        printf("Центральная буква: %c", word[length-1]);
    }
    else {
        printf("Центральная буква: %c", word[length]);
    }
 }