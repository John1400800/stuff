#include <stdio.h>

#define isspace(c)                              \
    ({ __typeof__ (c) _c = (c);                 \
     (_c>=9&&_c<=13)||_c==32; })

#define max(a, b)                               \
    ({ __typeof__ (a) _a = (a), _b = (b);       \
     _a > _b ? _a : _b; })

#define HEADER1 "other"
#define HEADER2 "separate"
#define HEADER3 "digits"

#define PRINT_HOR_LINE1()                       \
    do {                                        \
        for (i=0; i<2; ++i) {                   \
            putchar('+');                       \
            for (j=0; j<fiels_len[i]+2; ++j)    \
                putchar('-');                   \
        }                                       \
        printf("+\n");                          \
    } while (0)

int strlen(const char *s);
int count_dec_digits(int n);

int main(void) {
    int i, j, c, noth, nsep, ndig[10], fiels_len[2];
    /* input */
    for (i=0; i<10; ++i)
        ndig[i]=0;
    for (noth=nsep=0; (c = getchar()) != EOF; )
        if (c>='0' && c<='9')
            ++ndig[c-'0'];
        else if (isspace(c))
            ++nsep;
        else
            ++noth;
    /* field calculation */
    fiels_len[0]=max(max(strlen(HEADER1), strlen(HEADER2)), strlen(HEADER3));
    for (fiels_len[1]=count_dec_digits(ndig[0]),i=1; i<10; ++i)
        fiels_len[1]=max(fiels_len[1], count_dec_digits(ndig[i]));
    fiels_len[1]=max(max(fiels_len[1], count_dec_digits(noth)), count_dec_digits(nsep));
    /* draw table */
    PRINT_HOR_LINE1();
    printf("| %-*s|%*d |\n"                     /* draw values */
           "| %-*s|%*d |\n",
           fiels_len[0]+1, HEADER1, fiels_len[1]+1, noth,
           fiels_len[0]+1, HEADER2, fiels_len[1]+1, nsep);
    PRINT_HOR_LINE1();
    for (i=0; i<10; ++i)
        printf("| \'%d\'%-*s|%*d |\n",          /* draw values */
           i, fiels_len[0]-3+1, "", fiels_len[1]+1, ndig[i]);
    PRINT_HOR_LINE1();
    return 0;
}

/* log10() */
int count_dec_digits(int n) {
    int count;
    count=0;
    do
        ++count;
    while ((n/=10)>0);
    return count;
}

int strlen(const char *s) {
    int length;
    for (length=0; *s!='\0'; ++length)
        ++s;
    return length;
}
