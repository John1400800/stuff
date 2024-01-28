#include <stdio.h>
#include "get_num.h"

#define MAXLINE 100

int abs(int n) {
    return n >= 0 ? n : -n;
}

int main(void) {
    char buffs[MAXLINE+1];
    int n;

    printf("введите число: ");
    getline(buffs, MAXLINE);
    while (!isint(buffs) || abs(n = atoi(buffs)) >= 5) {
        printf("некоректный ввод, введите еще раз: ");
        getline(buffs, MAXLINE);
    }

    if (n >= 0) 
        switch (n) {
        case 0:
            printf("ноль");
            break;
        case 1:
            printf("один");
            break;
        case 2:
            printf("два");
            break;
        case 3:
            printf("четыре");
            printf("три");
            break;
        case 4:
            printf("четыре");
            break;
        }
    else
        printf("отрицаельное");
    
}
