#include <stdio.h>
#include "common.h"

static char is_digit(char c) {
    if (c >= '0' && c <= '9') {
        return NUM;
    }
    return UNKN;
}

static char is_operator(char c) {
    if (c == '+' || c == '-' || c == '*' || c == '/') {
        return OP;
    }
    return UNKN;
}

char get_next(char *buff) {
    static char prevch = ' ';
    unsigned i = 0;
    char type = UNKN;

    while (1)
    {
        if (prevch == ' ') {
            prevch = getchar();
            if (i == 0) {
                continue;
            }
        }
        buff[i] = prevch;
        if (is_digit(prevch) && (type == UNKN || type == NUM)) {
            type = NUM;
        } else if (is_operator(prevch) && type == UNKN) {
            type = OP;
        } else {
            break;
        }
        ++i;
        prevch = ' ';
    }
    if (type == UNKN) {
        ++i;
    }
    buff[i] = '\0';
    return type;
}
