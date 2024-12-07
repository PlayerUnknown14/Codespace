#include <stdio.h>
#include <string.h>


int main(){
    char text[100];
    char word[100];
    char* strpoiner = text;
    int count = 0;

    printf("\nВведите строку текста: ");
    scanf("%s", &text);
    puts(text);
    printf("\nВведите слово: ");
    scanf("%s", &word);
    puts(word);

    while ((strpoiner = strstr(strpoiner, word)) != NULL)
    {
            count++;
            strpoiner++;
    }

    printf("Указанное слово встречается в тексте %d раз.", count);
    getchar();
    return 0;
}

/*
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
*/