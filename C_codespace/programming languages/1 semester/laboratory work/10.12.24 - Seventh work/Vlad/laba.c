#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main(){
    int N, i;
    printf("\nВведите длину массива: ");
    scanf("%d", &N);

    char list[N];
    srand(time(NULL));
    for (i = 0; i < N; i++)
        int m = rand() % 10;
        list[i] = m;
    for (i = 0; i < N; i++)
        int m = list[i];
        printf("\nЭлемент массива = %s, адрес элемента = %p", m, &m);

    return 0;
}