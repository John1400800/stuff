#include <stdio.h>

int strlen_(char *s) {
    char *p = s;
    while (*p++)
        ;
    return (int)(p - s) - 1;
}

void strcpy_(char *s, char *t) {
    while ((*s++ = *t++))
        ;
}

int strcmp_(char *s, char *t) {
    for (; *s == *t; ++s, ++t)
        if (*s == '\0')
            return 0; // equal
    return *s - *t;
}

void strcat_(char *s, char *t) {
    while (*s != '\0')
        ++s;
    strcpy_(s, t);
}

int strend(char *ss, char *st) {
    char *ps = ss;
    char *pt = st;
    while (*ps)
        ++ps;
    while (*pt)
        ++pt;
    if (ps - ss < pt - st)
        return 0;
    ps -= pt - st;
    for (; *ps == *st; ++ps, ++st)
        if (*ps == '\0')
            return 1;
    return 0;
}

void strncpy_(char *s, char *t, int n) {
    char *st = t;
    for (; (*s = *t) && t - st < n; ++s, ++t)
        ;
    *s = '\0';
}

void strncat_(char *s, char *t, int n) {
    while (*s)
        ++s;
    strncpy_(s, t, n);
}

int main(void) {
    char s[1000] = "hello ";
    strncat_(s, "worldly", 5);
    strcat_(s, "!");
    printf("|%s|", s); 
}
