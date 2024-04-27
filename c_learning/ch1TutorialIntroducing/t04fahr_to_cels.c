#include <stdio.h>
#include <string.h>

#define LOWER          0
#define UPPER        300
#define STEP          20
#define TITLE1    "fahr"
#define TITLE2 "celsius"
#define PRINT_HOR_LINE() \
    do { \
        for (i=0; i<2; ++i) { \
            putchar('+'); \
            for (j=0; j<title_lengths[i]+1; ++j) \
                putchar('-'); \
            if (i==1) \
                printf("+\n"); \
        } \
    } while(0)

int main(void) {
    int i, j, fahr, title_lengths[2];
    title_lengths[0] = strlen(TITLE1);
    title_lengths[1] = strlen(TITLE2);

    PRINT_HOR_LINE();
    printf("| " TITLE1 "| " TITLE2 "|\n");
    PRINT_HOR_LINE();
    for (fahr=LOWER; fahr<=UPPER; fahr+=STEP)
        printf("| %*d| %*.1f|\n",
                title_lengths[0], fahr,
                title_lengths[1], (float)(fahr-32)*5.f/9.f);
    PRINT_HOR_LINE();
    return 0;
}
