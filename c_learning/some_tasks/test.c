#include <stdio.h>

#define OUT 0
#define IN  1

int main(void) {
    int c, nc, nw, nl, state;
    for (nc = nw = nl = 0, state = OUT; (c = getchar()) != EOF; ++nc)
        if (c == ' ' || c == '\t' || c == '\n') {
            if (c == '\n')
                ++nl;
            state = OUT;
        } else if (state == OUT) {
            ++nw;
            state = IN;
        }
    printf("number:\n"
           "lines: %d\n"
           "characters: %d\n"
           "words: %d\n",
           nl, nc, nw);
    return 0;
}
