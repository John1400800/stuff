#include <stdio.h>
#include <stdlib.h>

#include "get_num.h"

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
