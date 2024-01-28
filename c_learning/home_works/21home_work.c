/* clang version 15.0.1
 * Target: x86_64-pc-windows-msvc
 * Thread model: posix
 * InstalledDir: C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\Llvm\x64\bin
 * 
 * clang -Wall -Wextra -Wconversion -std=c99 .\get_float.c .\test.c
 *
 * -----------------------------------------------------------------------------
 *  test.c
 * ----------------------------------------------------------------------------- 
 */

#include <math.h>
#include <stdio.h>
#include "get_num.h"

#define MAXLINE 100
#define M_PI 3.14159265358979323846
#define deg_to_rad(deg) ((deg)*M_PI / 180)

int main(void) {
    char buffs[MAXLINE+1];
    double a, b, z1, z2;

    printf("введите угол а: ");
    getline(buffs, MAXLINE);
    while (!isfloat(buffs)) {
        printf("некоректный ввод, введите еще раз: ");
        getline(buffs, MAXLINE);
    }
    a = deg_to_rad(atof(buffs));

    printf("введите угол b: ");
    getline(buffs, MAXLINE);
    while (!isfloat(buffs)) {
        printf("некоректный ввод, введите еще раз: ");
        getline(buffs, MAXLINE);
    }
    b = deg_to_rad(atof(buffs));

    printf("z1 = %lf\nz2 = %lf",
           z1 = pow(cos(a) - cos(b), 2) - pow(sin(a) - sin(b), 2),
           z2 = -4 * pow(sin((a - b) / 2), 2) * cos(a + b));

    return 0;
}
