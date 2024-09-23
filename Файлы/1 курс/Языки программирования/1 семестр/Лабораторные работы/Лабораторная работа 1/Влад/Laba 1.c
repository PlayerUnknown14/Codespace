#include <stdio.h>
#include <math.h>

int main() {
    double a;
    printf("\nВведите переменную a: ");
    scanf("%lf", &a);
    double y = 1 - 1.0/4.0 * pow(sin(2*a), 2) + cos(2 * a);
    double z = pow(cos(a), 2) + pow(pow(cos(a), 2), 2);
    printf("Y = %lf\nZ = %lf", y, z);
    return 0;
}