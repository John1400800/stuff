#include <stdio.h>

#ifndef NULL
#define NULL ((void*)0)
#endif

#define MAXWORD 100

#define talloc() (struct tnode *)alloc(sizeof(struct tnode))
#define isspace(c) (((c) >= 9 && (c) <= 13) || (c) == 32)
#define isalnum(c)                                                             \
    (((c) >= '0' && (c) <= '9') || ((c) >= 'a' && (c) <= 'z') ||               \
     ((c) >= 'A' && (c) <= 'Z'))

struct tnode {
    char *word;
    int count;
    struct tnode *left;
    struct tnode *right;
};

struct tnode *addtree(struct tnode *, char *);
void treeprint(struct tnode *);
int getword(char *word, int lim);

int main(void) {
    struct tnode *root;
    char word[MAXWORD+1];

    root = NULL;
    while (getword(word, MAXWORD) > 0)
        root = addtree(root, word);
    treeprint(root);
    return 0;
}

char *strdup_(char *);
int strcmp_(char *s, char *t);

void *alloc(int n);

struct tnode *addtree(struct tnode *p, char *w) {
    int cond;

    if (p == NULL) {
        p = talloc();
        p->word = strdup_(w);
        p->count = 1;
        p->left = p->right = NULL;
    } else if ((cond = strcmp_(w, p->word)) == 0) 
        p->word++;
    else if (cond < 0)    
        p->left = addtree(p->left, w);
    else
        p->right = addtree(p->right, w);
    return p;
}

void treeprint(struct tnode *p) {
    if (p != NULL) {
        treeprint (p->left);
        printf("%4d %s\n", p->count, p->word);
        treeprint(p->right);
    }
}

int strcmp_(char *s, char *t) {
    for (; *s == *t; ++s, ++t)
        if (*s == '\0')
            return 0;
    return *s - *t;
}

int strlen_(char *);

char *strcpy_(char *s, char *t);

char *strdup_(char *s) {
    char *p;
    p = (char *)alloc(strlen_(s)+1);
    if (p != NULL)
        strcpy_(p, s);
    return p;
}

char *strcpy_(char *s, char *t) {
    char *p;
    for (p = s; (*p = *t) != '\0'; ++p, ++t)
        ;
    return s;
}


int getch(void);
void ungetch(int);

int getword(char *word, int lim) {
    char *w = word;
    char c;
    c = getch();
    while (isspace(c))
        c = getch();
    for (*w = c; lim-- > 0; ++w, *w = getch()) {
        if (!isalnum(*w)) {
            ungetch(*w);
            break;
        }
    }
    *w = '\0';
    return w - word;
}


#define SIZEBUF 100

static int buff[SIZEBUF];
static int *buffp = buff;

int getch(void) { return buffp > buff ? *--buffp : getchar(); }

void ungetch(int c) {
    if (buffp - buff < SIZEBUF) {
        int *p;
        for (p = buffp++; p > buff; --p)
            *p = *(p - 1);
        *buff = c;
    } else
        printf("\nungetch: buff owerflow!\n");
}


#define ALLOCSIZE 10000

static char allocbuf[ALLOCSIZE];
static char *allocp = allocbuf;

void *alloc(int n) {
    if (allocp - allocbuf + n <= ALLOCSIZE)
        return (void *)((allocp += n) - n);
    return NULL;
}

void afree(void *p) {
    if ((char *)p >= allocbuf && (char *)p < allocbuf + ALLOCSIZE)
        allocp = p;
}

int strlen_(char *ps) {
    char *p = ps;
    while (*p != '\0')
        ++p;
    return p - ps;
}
