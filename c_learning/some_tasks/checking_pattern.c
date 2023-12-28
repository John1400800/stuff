#include <stdio.h>

#define MAXLINE 1000
#define MAXSTR MAXLINE * 10

int str_index(char *source, char *pattern) {
    int i, j;
    for (i = 0; source[i] != '\0'; ++i) {
        for (j = 0; source[i + j] == pattern[j]; ++j)
            if (source[i + j] == '\0')
                return i;
        if (pattern[j] == '\0')
            return i;
    }
    return -1;
}

void copy(char *from, char *to, unsigned *pos, unsigned lim) {
    unsigned i = 0;
    while (*pos < lim && (to[(*pos)++] = from[i++]) != '\0')
        ;
    if (*pos < lim)
        (*pos)--;
    else
        to[*pos] = '\0';
}

unsigned getline(char *buff, unsigned lim) {
    unsigned i = 0;
    while (i < lim && (buff[i] = (char)getchar()) != '\n' && buff[i] != EOF) {
        ++i;
    }
    buff[i] = '\0';
    return i;
}

int main(void) {
    unsigned pos = 0;
    char res[MAXSTR + 1], buff[MAXLINE + 1];
    while (getline(buff, MAXLINE)) {
        if (str_index(buff, "ould") >= 0) {
            copy(buff, res, &pos, MAXSTR);
            copy("\n", res, &pos, MAXSTR);
        }
    }
    printf("%s", res);
    printf("%d", str_index("hello world ", "world"));
    return 0;
}
