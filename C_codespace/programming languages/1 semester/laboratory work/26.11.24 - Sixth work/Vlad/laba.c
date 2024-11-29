#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    char text[100], word[10], substr_pointer;
    int count = 0;
    printf("\nВведите строку текста: ");
    scanf("%s", &text);
    printf("\nВведите слово: ");
    scanf("%s", &word);
    substr_pointer = strstr(text, word);
    while (substr_pointer != NULL)
    {
            count++;
            strncpy(substr_pointer,"    ",4);
            substr_pointer = strstr(text, word);
    }

    printf("Указанное слово встречается в тексте %d раз.", count);

    return 0;
}