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

#include <string.h>
#include <stdio.h> 
#define SIZE 100                     
 
int main()
{
    char  s[SIZE];                  
    char  substr[SIZE];        
    int   n = 0;                 
    char* temp = s;                  
    
    puts("Vvedite stroku: \n");     
    gets(s);                        
    puts("\nVvedite slovo: \n"); 
    gets(substr);             
   
  
    while((temp = strstr(temp, substr)) != NULL) 
    {
                                    
        n++;                        
        temp++;                      
                                     
    }
    printf("\nEto slovo vstrechaetsya %d raz(a)!", n);
    getchar();
    return 0;
}