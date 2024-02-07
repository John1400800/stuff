#include <stdio.h>

#define isdigit(c) ((c) >= '0' && (c) <= '9')
#define isasciispace(c) (((c) >= 9 && (c) <= 13) || (c)==32)
#define itoa(n, s) (*ritoa((n), (s))='\0', (s))

int gcd(int a, int b);
double atof_(char *s);
char *ritoa(int n, char *res);

int main(void) {
    char res[10];
    printf("%s", itoa(127, res));
    // printf("%.20lf\n", atof_("-3.1234"));
}

char *ritoa(int n, char *res) {
    if (n/10)
        res = ritoa(n/10, res);
    *res = n%10+'0';
    return ++res;
}

double atof_(char *s) {
    double res, power, isstart;
    int sign;
    while (isasciispace(*s))
        ++s;
    sign = 0;
    if (*s == '+' || *s == '-') {
        sign = *s == '-' ? -1 : 1;
        ++s;
    }
    for (isstart = 1, res = 0, power = 0; isdigit(*s) || *s == '.'; ++s) {
        if (*s == '.') {
            if (power || (isstart && sign)) {
                printf("err");
                return 0.0; // error: the second point was encountered
            }
            power = 1;
            continue;
        }
        if (!power)
            res = res * 10 + *s - '0';
        else
            res += (*s - '0') / (power *= 10);
        if (isstart)
            isstart = 0;
    }
    if (isstart && sign)
        return 0.0; // error sign without number
    if (sign == -1 && res == 0)
        return 0.0; // error -0 not supported
    return (sign ? sign : 1) * res;
}

#define SWAP(type, a, b)                                                       \
    do {                                                                       \
        type temp = a, a = b, b = temp;                                        \
    } while (1)

int gcd(int a, int b) {
    if (b > a)
        SWAP(int, a, b);
    while ((a = a % b) != 0)
        SWAP(int, a, b);
    return b;
}
