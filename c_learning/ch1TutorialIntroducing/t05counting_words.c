#include <stdio.h>

#define isspace(c) ((c)==' '||(unsigned)(c)-'\t'<5)

enum { OUT, IN };

int main(void) {
    int state, c, nw;
    for (nw=0, state=OUT; (c=getchar())!=EOF; )
        if (isspace(c))
            state=OUT;
        else if (state==OUT) {
            ++nw;
            state=IN;
        }
    printf("%d\n", nw);
    return 0;
}
