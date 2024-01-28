// /* clang version 15.0.1
//  * Target: x86_64-pc-windows-msvc
//  * Thread model: posix
//  * InstalledDir: C:\Program Files\Microsoft Visual
//  Studio\2022\Community\VC\Tools\Llvm\x64\bin
//  *
//  * clang -Wall -Wextra -Wconversion -std=c99 get_float.c main.c
//  *
//  * -----------------------------------------------------------------------------
//  *  get_float.c
//  * -----------------------------------------------------------------------------
//  */

// #ifndef _INC_STDIO
// #include <stdio.h>
// #endif
// #define is_space(c) (((c) >= 9 && (c) <= 13) || (c) == 32)
// #define is_digit(c) ((c) >= '0' && (c) <= '9')

// long long getline(char *s, int lim) {
//     char *ps = s;
//     while (ps < s + lim && (*ps = (char)getchar()) != '\n')
//         ++ps;
//     *ps = '\0';
//     return ps - s;
// }

// int isfloat(char *s) {
//     int is_dot = 0;
//     char *ps;
//     while (is_space(*s))
//         ++s;
//     for (ps = s; *ps != '\0'; ++ps) {
//         if (!is_digit(*ps) && !(*ps == '.' && !is_dot) &&
//             !(*ps == '-' && ps == s))
//             return 0;
//         if (*ps == '.')
//             is_dot = 1;
//     }
//     if (ps > s && !((*s == '.' || *s == '-') && ps == s + 1) &&
//         !(*s == '-' && *(s + 1) == '.' && ps == s + 2))
//         return 1;
//     return 0;
// }

// double atof_(char *s) {
//     char *ps;
//     int res, sign, pow_;
//     while (is_space(*s))
//         ++s;
//     sign = 1;
//     if (*s == '-' || *s == '+') {
//         if (*s == '-')
//             sign = -1;
//         ++s;
//     }
//     for (ps = s, res = 0, pow_ = 0; is_digit(*ps) || *ps == '.'; ++ps)
//         if (*ps == '.')
//             pow_ = 1;
//         else {
//             res = res * 10 + *ps - '0';
//             pow_ *= 10;
//         }
//     return (double)(res * sign) / (double)(pow_ ? pow_ : 1);
// }

// /*
// -----------------------------------------------------------------------------
//  *  get_float.h
//  * -----------------------------------------------------------------------------
//  */

// int getline(char *s, int lim);
// int isfloat(char *s);
// double atof_(char *s);

// #ifndef _INC_MATH
// #define atof(ps) (atof_(ps))
// #endif

// /*
// -----------------------------------------------------------------------------
//  *  main.c
//  * -----------------------------------------------------------------------------
//  */
// #include <math.h>
// #include <stdio.h>
// #include "get_float.h"

// #define MAXLINE 100
// #define M_PI 3.14159265358979323846
// #define deg_to_rad(deg) ((deg)*M_PI / 180)

// int main(void) {
//     char buffs[MAXLINE+1];
//     double a, b, z1, z2;

//     printf("введите угол а: ");
//     getline(buffs, MAXLINE);
//     while (!isfloat(buffs)) {
//         printf("некоректный ввод, введите еще раз: ");
//         getline(buffs, MAXLINE);
//     }
//     a = deg_to_rad(atof(buffs));

//     printf("введите угол b: ");
//     getline(buffs, MAXLINE);
//     while (!isfloat(buffs)) {
//         printf("некоректный ввод, введите еще раз: ");
//         getline(buffs, MAXLINE);
//     }
//     b = deg_to_rad(atof(buffs));

//     printf("z1 = %lf\nz2 = %lf",
//            z1 = pow(cos(a) - cos(b), 2) - pow(sin(a) - sin(b), 2),
//            z2 = -4 * pow(sin((a - b) / 2), 2) * cos(a + b));

//     return 0;
// }

#include <stdio.h>
#include <stdlib.h>
#include "get_float.h"

#define MAXLINE 100

typedef struct point {
    double x;
    double y;
} Point;

typedef struct circle {
    double radius;
    struct point *center;
} Circle;

#define point_init(Point_, x_, y_)                                             \
    (Point_).x = (x_);                                                         \
    (Point_).y = (y_)

#define circle_init_(Circle_, r_, x_, y_)                                      \
    (Circle_).radius = (r_);                                                   \
    (Circle_).center = (Point *)malloc(sizeof(Point));                         \
    point_init(*(Circle_).center, (x_), (y_))

void circle_init(Circle *c) {
    char buffs[MAXLINE + 1];
    double x, y, r;
    printf("введите радиус: ");
    getline(buffs, MAXLINE);
    while (!isfloat(buffs) || (r = atof(buffs)) <= 0.0) {
        printf("некоректный ввод, введите еще раз: ");
        getline(buffs, MAXLINE);
    }
    printf("введите x: ");
    getline(buffs, MAXLINE);
    while (!isfloat(buffs)) {
        printf("некоректный ввод, введите еще раз: ");
        getline(buffs, MAXLINE);
    }
    x = atof(buffs);
    printf("введите y: ");
    getline(buffs, MAXLINE);
    while (!isfloat(buffs)) {
        printf("некоректный ввод, введите еще раз: ");
        getline(buffs, MAXLINE);
    }
    y = atof(buffs);
    circle_init_(*c, r, x, y);
}
unsigned intersect_of_circls(const Circle *c1, const Circle *c2) {
    double sq_dist_centers =
        ((c1->center->x - c2->center->x) * (c1->center->x - c2->center->x) +
         (c1->center->y - c2->center->y) * (c1->center->y - c2->center->y));
    double sq_summ_radii =
        (c1->radius + c2->radius) * (c1->radius + c2->radius);
    if (sq_dist_centers > sq_summ_radii)
        return 0;
    else if (sq_dist_centers == sq_summ_radii)
        return 1;
    else if (sq_dist_centers > 0)
        return 2;
    else if (c1->radius == c2->radius)
        return 3;
    else
        return 0;
}

int main(void) {
    unsigned n;
    Circle c1, c2;

    printf("1 окружность\n");
    circle_init(&c1);
    printf("2 окружность\n");
    circle_init(&c2);
    n = intersect_of_circls(&c1, &c2);
    printf(n < 3 ? "%d " : "бесконечность ", n);
    printf("пересечени");
    switch (n) {
    case 0:
    case 3:
        printf("й\n");
        break;
    case 1:
        printf("е\n");
        break;
    case 2:
        printf("я\n");
        break;
    }
}
