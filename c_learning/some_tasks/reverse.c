#include <stdio.h>

#define swap(T, a, b)                                                          \
    {                                                                          \
        static T __temp;                                                       \
        __temp = (a);                                                          \
        (a) = (b);                                                             \
        (b) = __temp;                                                          \
    }

long long str_len(char *s);
char *reverse_str(char *s);

int main(void) {
    char s[] = "hello world!";
    printf("%s", reverse_str(s));
}

long long str_len(char *s) {
    char *sp;
    for (sp = s; *sp != '\0'; ++sp)
        ;
    return sp - s;
}

char *reverse_str(char *s) {
    char *high, *low;
    for (low = s, high = s + str_len(s) - 1; low < high; ++low, --high)
        swap(char, *low, *high);
    return s;
}
