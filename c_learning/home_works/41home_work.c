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

#define is_inside(Circle_, Point_)                                             \
    ((Point_).x - (Circle_).center->x) * ((Point_).x - (Circle_).center->x) +  \
    ((Point_).y - (Circle_).center->y) * ((Point_).y - (Circle_).center->y) <  \
    Circle_.radius *Circle_.radius

int main(void) {
    unsigned i, n;
    char buffs[MAXLINE + 1];
    Circle c1;
    Point curr_p;

    printf("окружность:\n");
    circle_init(&c1);

    for (i = 0, n = 0; i < 10; ++i) {
        printf("точка %d:\n", i + 1);
        printf("введите x: ");
        getline(buffs, MAXLINE);
        while (!isfloat(buffs)) {
            printf("некоректный ввод, введите еще раз: ");
            getline(buffs, MAXLINE);
        }
        curr_p.x = atof(buffs);
        printf("введите y: ");
        getline(buffs, MAXLINE);
        while (!isfloat(buffs)) {
            printf("некоректный ввод, введите еще раз: ");
            getline(buffs, MAXLINE);
        }
        curr_p.y = atof(buffs);

        if (is_inside(c1, curr_p))
            ++n;
    }
    printf("%d", n);
    return 0;
}
