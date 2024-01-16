#include <math.h>
#include <stdio.h>

#define MAXLINE 100
#define M_PI 3.14159265358979323846
#define is_space(c) (((c) >= 9 && (c) <= 13) || (c) == 32)
#define is_digit(c) ((c) >= '0' && (c) <= '9')
#define deg_to_rad(deg) ((deg)*M_PI / 180)

int isfloat(char *s);
int getline(char *s, int lim);
double atof_(char *s);

int main(void) {
    char buffs[MAXLINE + 1];
    double a, b, z1, z2;

    printf("введите угол а: ");
    getline(buffs, MAXLINE);
    while (!isfloat(buffs))
        getline(buffs, MAXLINE);
    a = deg_to_rad(atof_(buffs));

    printf("введите угол b: ");
    getline(buffs, MAXLINE);
    while (!isfloat(buffs))
        getline(buffs, MAXLINE);
    b = deg_to_rad(atof_(buffs));

    printf("z1 = %f\nz2 = %f",
           z1 = pow(cos(a) - cos(b), 2) - pow(sin(a) - sin(b), 2),
           z2 = -4 * pow(sin((a - b) / 2), 2) * cos(a + b));

    return 0;
}

int getline(char *s, int lim) {
    char *ps = s;
    while (ps < s + lim && (*ps = getchar()) != '\n')
        ++ps;
    *ps = '\0';
    return ps - s;
}

int isfloat(char *s) {
    int is_dot = 0;
    char *ps;
    while (is_space(*s))
        ++s;
    for (ps = s; *ps != '\0'; ++ps) {
        if (!is_digit(*ps) && !(*ps == '.' && !is_dot) &&
            !(*ps == '-' && ps == s))
            return 0;
        if (*ps == '.')
            is_dot = 1;
    }
    if (ps > s && !((*s == '.' || *s == '-') && ps == s + 1) &&
        !(*s == '-' && *(s + 1) == '.' && ps == s + 2))
        return 1;
    return 0;
}

double atof_(char *s) {
    char *ps;
    int res, sign, pow_;
    while (is_space(*s))
        ++s;
    sign = 1;
    if (*s == '-' || *s == '+') {
        if (*s == '-')
            sign = -1;
        ++s;
    }
    for (ps = s, res = 0, pow_ = 0; is_digit(*ps) || *ps == '.'; ++ps)
        if (*ps == '.')
            pow_ = 1;
        else {
            res = res * 10 + *ps - '0';
            pow_ *= 10;
        }
    return (double)(res * sign) / (double)(pow_ ? pow_ : 1);
}
