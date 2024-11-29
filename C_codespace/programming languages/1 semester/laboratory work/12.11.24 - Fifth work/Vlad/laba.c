// НАПИСАТЬ СВОЙ АЛГОРИТМ СОРТИРОВКИ ЭЛЕМЕНТОВ
#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b) {
    return (*(int*)b - *(int*)a);
}

int main() {
    int N, i;
    int k1 = 0;
    int k2 = 0;
    int k3 = 0;

    printf("Укажите количество элементов вашего массива: ");
    scanf("%d", &N);
    int X[N];

    printf("Введите %d чисел (через пробел): ", N);
    for(i = 0; i < N; i++)
        scanf("%d", &X[i]);
    int n = sizeof(X) / sizeof(int);
    qsort(X, n, sizeof(int), compare);
    printf("Упорядоченный по убыванию массив: ");
    for (i = 0; i < N; i++)
        {
            printf("%d ", X[i]);
            if (X[i] > 0)
                k1++;
            else if (X[i] < 0)
                k2++;
            else
                k3++;
        };
    printf("\nКоличество положительных элементов - %d\nКоличество отрицательных элементов - %d\nКоличество нулевых элементов - %d", k1, k2, k3);
    
    return 0;
}