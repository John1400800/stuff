#include <stdio.h>
#include "get_num.h"

#define M_PI 3.14159265358979323846
#define MAXLINE 100
#define ball_volume(r) (4. / 3. * M_PI * ((r) * (r) * (r)))
#define ball_surface_area(r) (4 * M_PI * (r) * (r))
#define max(a, b) (((a) > (b)) ? (a) : (b))
#define min(a, b) (((a) < (b)) ? (a) : (b))

int main(void) {
    char buffs[MAXLINE + 1];
    double v1, v2, r1, r2;

    printf("введите радиус r1: ");
    getline(buffs, MAXLINE);
    while (!isfloat(buffs)) {
        printf("некоректный ввод, введите еще раз: ");
        getline(buffs, MAXLINE);
    }
    r1 = atof(buffs);

    printf("введите радиус r2: ");
    getline(buffs, MAXLINE);
    while (!isfloat(buffs)) {
        printf("некоректный ввод, введите еще раз: ");
        getline(buffs, MAXLINE);
    }
    r2 = atof(buffs);

    v1 = ball_volume(r1);
    v2 = ball_volume(r2);
    printf("объем полого шара: %f\nполная поверхность полого шара: %f",
           max(v1, v2) - min(v1, v2), ball_surface_area(r1)+ball_surface_area(r2));
}
