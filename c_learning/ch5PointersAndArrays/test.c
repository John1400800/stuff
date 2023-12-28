#include <stdio.h>

#define OUT       0
#define IN        1
#define MAXLENGTH 1000
#define isspace(C) (((C) >= 9 && (C) <= 13) || (C) == 32)

void makehist(char *str, unsigned *hist);
void hprinthist(unsigned *hist, unsigned lim);
void vprinthist(unsigned *hist, unsigned lim);

void printd(unsigned n, unsigned rspcs);

int main(void) {
    char s[MAXLENGTH+1] = "* ***** *** ****** **** ** *** *** *** **"
                          "***** ** *** ** **** *** *** **** ***** *"
                          "** *** * * *** **** * *******************";
    unsigned hist[MAXLENGTH+1] = {};
    makehist(s, hist);
    vprinthist(hist, MAXLENGTH);
    return 0;
}

void makehist(char *str, unsigned *hist) {
    char islastspace = 1;
    unsigned i, curr_length = 0;
    for (i = 0; str[i] != '\0'; ++i) {
        if (!isspace(str[i])) {
            ++curr_length;
            islastspace = 0;
        } else if (!islastspace) {
            ++hist[curr_length];
            curr_length = 0;
            islastspace = 1;
        }
    }
    ++hist[curr_length];
}

unsigned ndigits(unsigned n) {
    unsigned cnt_digits = 0;
    do {
        ++cnt_digits;
    } while (n /= 10);
    return cnt_digits;
}

void printd(unsigned n, unsigned rspcs) {
    if (n / 10) {
        printd(n / 10, rspcs);
    } else {
        while (rspcs-- > 0) {
            putchar(' ');
        }
    }
    putchar((char)(n%10 + '0'));
}

void vprinthist(unsigned *hist, unsigned lim) {
    char is_cntn;
    unsigned i, curr_cnt, nspcs;
    for (i = 1; i <= lim; ++i) {
        if (hist[i] > 0) {
            printd(i, 0);
            putchar(' ');
        }
    }
    putchar('\n');
    is_cntn = 1;
    curr_cnt = 1;
    while (is_cntn) {
        is_cntn = 0;
        for (i = 1; i <= lim; i++) {
            if (hist[i] > 0) {
                nspcs = ndigits(i);
                while(--nspcs > 0) {
                    putchar(' ');
                }
                if (hist[i] >= curr_cnt) {
                    putchar('*');
                    is_cntn = 1;
                } else {
                    putchar(' ');
                }
                putchar(' ');
            }
        }
        putchar('\n');
        ++curr_cnt;
    }
    
}

void hprinthist(unsigned *hist, unsigned lim) {
    unsigned i, j;
    for (i = 1; i <= lim; ++i) {
        if (hist[i] > 0) {
            printf("%d: ", i);
            for (j = 0; j < hist[i]; ++j) {
                putchar('*');
            }
            putchar('\n');
        }
     }
}

