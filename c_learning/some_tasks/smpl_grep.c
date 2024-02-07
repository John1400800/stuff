#include <stdio.h>
#include <stdlib.h>

#ifndef NULL
#define NULL ((void *)0)
#endif
#define MAXLINE 100
#define LINES 100
#define upper(c) ((c) >= 'a' && (c) <= 'z' ? 'A' + (c) - 'a' : (c))

char *str_str(char *s, char *t);
int sgetline(char *buff, int lim, int *len);
char *str_cpy(char *s, char *t);

int main(int argc, char *argv[]) {
    char sbuff[MAXLINE + 1], *lines[LINES], *sub_start;
    int i, j, k, cur_len;
    if (argc == 1) {
        printf("input pattern as run paramtr!");
        return 1;
    }
    for (i = 0; i < LINES; ++i) {
        if (sgetline(sbuff, MAXLINE, &cur_len) == EOF) {
            lines[i] = NULL;
            break;
        }
        lines[i] = str_cpy(malloc(sizeof(char) * (cur_len + 1)), sbuff);
    }
    for (i = 0; i < LINES && lines[i] != NULL; ++i) {
        sub_start = str_str(lines[i], argv[1]);
        if (argc > 1 && sub_start != NULL) {
            for (j = k = 0; lines[i][j] != '\0'; ++j) {
                if (&lines[i][j] >= sub_start && argv[1][k] != '\0') {
                    putchar(upper(argv[1][k]));
                    ++k;
                } else
                    putchar(lines[i][j]);
            }
            putchar('\n');
        }
    }
}

char *str_str(char *s, char *t) {
    char *tp;
    for (; *s != '\0'; ++s) {
        for (tp = t; *tp != '\0' && *(s + (tp - t)) == *tp; ++tp)
            ;
        if (*tp == '\0')
            return s;
    }
    return NULL;
}

int sgetline(char *buff, int lim, int *len) {
    char c;
    for (*len = 0; (c = getchar()) != '\n' && c != EOF; --lim)
        if (lim)
            buff[(*len)++] = c;
    buff[*len] = '\0';
    return c;
}

char *str_cpy(char *s, char *t) {
    char *sp;
    for (sp = s; (*sp = *t) != '\0'; ++sp, ++t)
        ;
    return s;
}
