#include <stdio.h>

#define SIZE 4
#define isspace(c) (((c) >= 9 && (c) <= 13) || (c) == 32)
#define isdigit(c) ((c) >= '0' && (c) <= '9')

#define BUFFSIZE 100
static int buf[BUFFSIZE];
static int bufp = 0;

int getch(void) { return (bufp > 0) ? buf[--bufp] : getchar(); }

void ungetch(int c) {
    if (bufp >= BUFFSIZE) 
        printf("ungetch: too many characters");
    else 
        buf[bufp++] = c;
    
}

int getint(int *pn) {
    int c, sign = 1;
    c = getch();
    while (isspace(c))
        c = getch();
    if (!isdigit(c) && c != '-' && c != '+') {
        ungetch(c);
        return 0;
    }
    if (c == '-' || c == '+') {
        if (c == '-')
            sign = -1;
        c = getch();
    }
    *pn = 0;
    while (isdigit(c)) {
        *pn = *pn * 10 + (c - '0');
        c = getch();
    }
    *pn *= sign;
    ungetch(c);
    return c;
}

int main(void) {
    int i, array[SIZE], is_num;

    for (i = 0; i < SIZE && (is_num = getint(&array[i])) != EOF; ++i)
        ;

    for (i = 0; i < SIZE; ++i) 
        printf("%d%s ", array[i], i != SIZE - 1 ? "," : "");
    
    return 0;
}
