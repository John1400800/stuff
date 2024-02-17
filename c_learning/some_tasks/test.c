#include <stdio.h>

#define OUT 0
#define IN  1

int main(void) {
    int i, c, nc, nw, nl, nd[10], state;
    for (i = 0; i < 10; ++i)
        nd[i] = 0;
    for (nc = nw = nl = 0, state = OUT; (c = getchar()) != EOF; ++nc)
        if (c == ' ' || c == '\t' || c == '\n') {
            if (c == '\n')
                ++nl;
            state = OUT;
        } else {
            if (c >= '0' && c <= '9')
                ++nd[c & 0x0f];
            if (state == OUT){
                ++nw;
                state = IN;
            }
        }
    printf("number:\n"
           "lines: %d\n"
           "characters: %d\n"
           "words: %d\n",
           nl, nc, nw);
    printf("digits: 0 1 2 3 4 5 6 7 8 9\n%-8s", "");
    for (i = 0; i < 10; ++i)
        printf("%d ", nd[i]);
    putchar('\n');
    return 0;
}
