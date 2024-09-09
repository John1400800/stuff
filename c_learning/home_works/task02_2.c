#include <math.h>
#include <stdio.h>
#include "get_num.h"

#define MAXLINE 100
#define M_PI 3.14159265358979323846

int main(void) {
    char buffs[MAXLINE + 1];
    double a, b, area; // a -> width, b -> ratio of radii

    printf("введите ширину кольца (a): ");
    getline(buffs, MAXLINE);
    while (!isfloat(buffs)) {
        printf("некоректный ввод, введите еще раз: ");
        getline(buffs, MAXLINE);
    }
    a = atof(buffs);

    printf("введите отношение радиусов (b): ");
    getline(buffs, MAXLINE);
    while (!isfloat(buffs)) {
        printf("некоректный ввод, введите еще раз: ");
        getline(buffs, MAXLINE);
    }
    b = atof(buffs);

    printf("%lf", area = (M_PI * pow(a, 2) * (b + 1)) / (b - 1));
    return 0;
}
