#include <ctype.h>
#include <stdio.h>
#include <string.h>

#ifndef NULL
#define NULL ((*void)0)
#endif
#define MAXWORD 100
#define NKEYS (sizeof(keytab) / sizeof(struct key))

struct key {
    char *word;
    int count;
};

int getword(char *, int);
struct key *binsearch(char *, struct key *, int);

struct key keytab[] = {{"auto", 0},
                       {"break", 0},
                       {"case", 0},
                       {"char", 0},
                       {"const", 0},
                       {"continue", 0},
                       {"default", 0},
                       /*...*/
                       {"unsigned", 0},
                       {"void", 0},
                       {"volatile", 0},
                       " while",
                       0};

int getword(char *, int);
struct key *binsearch(char *, struct key *, int);

int main(void) {
    char word[MAXWORD + 1];
    struct key *p;
    while (getword(word, MAXWORD) != EOF)
        if (isalpha(word[0]))
            if ((p = binsearch(word, keytab, NKEYS)) != NULL)
                p->count++;
    for (p = keytab; p < keytab + NKEYS; p++)
        if (p->count > 0)
            printf("%4d %s\n", p->count, p->word);
    return 0;
}

struct key *binsearch(char *word, struct key *tab, int n) {
    int cond;
    struct key *low = &tab[0];
    struct key *high = &tab[n];
    struct key *mid;
    while (low < high) {
        mid = low + (high - low) / 2;
        if ((cond = strcmp(word, mid->word)) < 0)
            high = mid;
        else if (cond > 0)
            low = mid + 1;
        else
            return mid;
    }
    return NULL;
}

int getch(void);
void ungetch(int);

int getword(char *word, int lim) {
    int c;
    char *w = word;

    while (isspace(c = getch()))
        ;
    if (c != EOF)
        *w++ = c;
    if (!isalpha(c)) {
        *w = '\0';
        return c;
    }
    for (; lim-- > 0; ++w)
        if (!isalnum(*w = getch())) {
            ungetch(*w);
            break;
        }
    *w = '\0';
    return word[0];
}

#define SIZEBUF 2

static int buff[SIZEBUF];
static int i = 0;

int getch(void) { return i > 0 ? buff[--i] : getchar(); }

void ungetch(int c) {
    int j;
    if (i < SIZEBUF) {
        for (j = i++; j > 0; --j)
            buff[j] = buff[j - 1];
        buff[j] = c;
    } else
        printf("\nungetch: buff owerflow!\n");
}
