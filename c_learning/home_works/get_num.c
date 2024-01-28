#include <stdio.h>

#ifndef _INC_CTYPE
#define isspace(c) (((c) >= 9 && (c) <= 13) || (c) == 32)
#define isdigit(c) ((c) >= '0' && (c) <= '9')
#endif

long long getline(char *s, int lim) {
    char *ps = s;
    while (ps < s + lim && (*ps = (char)getchar()) != '\n')
        ++ps;
    *ps = '\0';
    return ps - s;
}

int isfloat(char *s) {
    int is_dot = 0;
    char *ps;
    while (isspace(*s))
        ++s;
    for (ps = s; *ps != '\0'; ++ps) {
        if (!isdigit(*ps) && !(*ps == '.' && !is_dot) &&
            !(*ps == '-' && ps == s))
            return 0;
        if (*ps == '.')
            is_dot = 1;
    }
    if (ps > s && !((*s == '.' || *s == '-') && ps == s + 1) &&
        !(*s == '-' && *(s + 1) == '.' && ps == s + 2))
        return 1;
    return 0;
}

int isint(char *s) {
    char *ps;
    while (isspace(*s))
        ++s;
    for (ps = s; *ps != '\0'; ++ps)
        if (!isdigit(*ps) && !(*ps == '-' && ps == s))
            return 0;
    if (ps > s && !(*s == '-' && ps == s+1))
        return 1;
    return 0;
}

double atof_(char *s) {
    int res, sign, pow_;
    while (isspace(*s))
        ++s;
    sign = 1;
    if (*s == '-' || *s == '+') {
        if (*s == '-')
            sign = -1;
        ++s;
    }
    for (res = 0, pow_ = 0; isdigit(*s) || *s == '.'; ++s)
        if (*s == '.')
            pow_ = 1;
        else {
            res = res * 10 + *s - '0';
            pow_ *= 10;
        }
    return (double)(res * sign) / (double)(pow_ ? pow_ : 1);
}

int atoi_(char *s) {
    int sign, res;
    while (isspace(*s))
        ++s;
    sign = 1;
    if (*s == '-' || *s == '+') {
        if (*s == '-')
            sign = -1;
        ++s;
    }
    for (res = 0; isdigit(*s); ++s)
        res = res * 10 + *s - '0';
    return res * sign;
}
