#include <stdio.h>

// work only for ASCII
#define isspase(c) (((c) >= 9 && (c) <= 13) || (c) == 32)

#define MAXLINE 1000

unsigned ndigits(unsigned n) {
    unsigned num = 1;
    while ((n /= 10) > 0) {
        ++num;
    }
    return num;
}

void rprintd(unsigned n) {
    if (n / 10 > 0) {
        rprintd(n / 10);
    }
    putchar(n % 10 + '0');
}

unsigned get_str(char *s, unsigned lim) {
    unsigned i, c, lastc;
    lastc = '\n';
    for (i = 0; i < lim && (c = getchar()) != EOF; ++i) {
        if (c == '\n' && lastc == '\n') {
            break;
        }
        s[i] = c;
        lastc = c;
    }
    s[i] = '\0';
    return i;
}

void count_all(char *s, int *nwhite, int *nother, int *ndigit) {
    int i;
    *nwhite = *nother = 0;
    // init 0 each pos of ndigit
    for (i = 0; i < 10; ++i) {
        ndigit[i] = 0;
    }
    // count all
    for (i = 0; s[i] != '\0'; ++i) {
        switch (s[i]) {
        case '0': case '1': case '2': case '3': case '4':
        case '5': case '6': case '7': case '8': case '9':
            ++ndigit[s[i] - '0'];
            break;
        case ' ':
        case '\t':
        case '\n':
            ++*nwhite;
            break;
        default:
            ++*nother;
            break;
        }
    }
}

int main(void) {
    char s[MAXLINE + 1];
    int i, ns, nwhite, nother, ndigit[10];
    get_str(s, MAXLINE);
    count_all(s, &nwhite, &nother, ndigit);
    // print all count
    printf("digit: ");
    for (i = 0; i < 10; ++i) {
        if (ndigit[i] > 0) {
            ns = putchar(ndigits(ndigit[i]) - 1);
            while (ns-- > 0) {
                putchar(' ');
            }
            rprintd((unsigned)i);
            putchar(' ');
        }
    }
    putchar('\n');
    printf("count: ");
    for (i = 0; i < 10; ++i) {
        if (ndigit[i] > 0) {
            rprintd((unsigned)ndigit[i]);
            putchar(' ');
        }
    }
    putchar('\n');
    printf("nwhite = %d\nnother = %d", nwhite, nother);
    return 0;
}
