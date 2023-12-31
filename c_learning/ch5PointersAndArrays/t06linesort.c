#include <stdio.h>

#ifndef NULL
#define NULL ((void *)0)
#endif
#define MAXLINES 100

char *lineptr[MAXLINES];

int readlines(char *strptr[], int maxlines);
void writelines(char *strptr[], int nlines);
void qsort(char *v[], int left, int right);

int main(void) {
    int nlines;

    if ((nlines = readlines(lineptr, MAXLINES)) >= 0) {
        qsort(lineptr, 0, nlines-1);
        writelines(lineptr, nlines);
        return 0;
    }
    printf("to many lines");
    return 1;
}

void writelines(char *strptr[], int nlines) {
    while (nlines--) {
        printf("%s", *strptr++);
        putchar('\n');
    }
}

int strcmp_(char *s, char *t);
void swap(char *v[], int i, int j) {
    char *temp;
    temp = v[i];
    v[i] = v[j];
    v[j] = temp;
}

void qsort(char *v[], int left, int right)
{
    int i, last;
    void swap(char *v[], int i, int j);


    if (left >= right) /* nothing is done if */
        return;        /* there are less than two elements in the array */

    swap(v, left, (left+right)/2);
    last = left;
    for(i = left+1; i <= right; i++)
        if (strcmp_(v[i], v[left]) < 0)
            swap(v, ++last, i);
    swap(v, left, last);
    qsort(v, left, last-1);
    qsort(v, last+1, right);
}

int strcmp_(char *s, char *t) {
    while (*s == *t) {
        if (*s == '\0')
            return 0; // equal
    }
    return *s - *t;
}

#define MAXLINE 100

int getline(char *s, int lim);
char *alloc(int n);
void strcpy_(char *s, char *t);

int readlines(char *strptr[], int maxlines) {
    int len, nlines;
    char *p, line[MAXLINE + 1];
    nlines = 0;
    while ((len = getline(line, MAXLINE)) > 0) {
        if (nlines >= maxlines || (p = alloc(len + 1)) == NULL)
            return -1; // to many lines or aloocbuf owerflow
        strcpy_(p, line);
        strptr[nlines++] = p;
    }
    return nlines;
}

int getline(char *s, int lim) {
    int n;
    for (n = 0; n < lim && (*s = (char)getchar()) != '\n'; ++n, ++s)
        ;
    *s = '\0';
    return n;
}

void strcpy_(char *s, char *t) {
    while ((*s++ = *t++) != '\0')
        ;
}

#define ALLOCSIZE MAXLINES *(MAXLINE + 1)

static char allocbuf[ALLOCSIZE];
static char *allocp = allocbuf;

char *alloc(int n) {
    if (allocp + n <= allocbuf + ALLOCSIZE)
        return (allocp += n) - n;
    return NULL;
}

int afree(char *p) {
    if (p >= allocbuf && p < allocbuf + ALLOCSIZE) {
        allocp = p;
        return 1;
    }
    return 0; // the free pointer goes beyond the alloc buffer
}
