#include <stdio.h>

#define hextou(c)                                                              \
    (((c) >= 'a' && (c) <= 'f')   ? ((c) - 'a' + 10)                           \
     : ((c) >= 'A' && (c) <= 'F') ? ((c) - 'A' + 10)                           \
                                  : ((c) - '0'))

#ifdef _INC_STDIO
#define dprintrgb(_Color)                                                      \
    do {                                                                       \
        int i;                                                                 \
        printf("rgb: ");                                                       \
        for (i = 0; i < 3; ++i)                                                \
            printf(i != 2 ? "%d, " : "%d", (i == 0)   ? (_Color).r             \
                                           : (i == 1) ? (_Color).g             \
                                                      : (_Color).b);           \
        putchar('\n');                                                         \
    } while (0)

#define hprintrgb(_Color)                                                      \
    do {                                                                       \
        int i, j, cv;                                                          \
        printf("hex: ");                                                       \
        for (i = 0; i < 3; ++i)                                                \
            for (j = 1; j >= 0; --j)                                           \
                if ((cv = ((*((char *)(&(_Color)) + i) >> (4 * j)) & 0x0f)) <  \
                    10)                                                        \
                    printf("%d", cv);                                          \
                else                                                           \
                    printf("%c", cv - 10 + 'a');                               \
        putchar('\n');                                                         \
    } while (0)
#endif

#define MAXLINE 100

typedef struct {
    unsigned char r, g, b;
} rgbColor;

int hextorgb(const char *hex, rgbColor *result);
int get_line(char *buff, int lim);

int main(void) {
    char sbuff[MAXLINE+1];
    rgbColor c;
    get_line(sbuff, MAXLINE);      // <-|-safty inp
    while (!hextorgb(sbuff, &c)) { // <-|
        printf("try again: ");     // <-|
        get_line(sbuff, MAXLINE);  // <-|
    }                              // <-|
    hextorgb(sbuff, &c);
    dprintrgb(c);
    return 0;
}

int hextorgb(const char *hex, rgbColor *result) {
    int i, j;
    if (hex[5] == '\0' || hex[6] != '\0')
        return 0; // ERROR
    for (i = 0; i < 6; i+=2) {
        *((char *)result + i / 2)=0;
        for (j = 0; j < 2; ++j) {
            if ((hex[i+j] < '0' || hex[i+j] > '9') &&
                (hex[i+j] < 'a' || hex[i+j] > 'z') &&
                (hex[i+j] < 'A' || hex[i+j] > 'Z'))
                    return 0; // ERROR
            *((char *)result + i / 2) =
                *((char *)result + i / 2) * 16 + hextou(hex[i+j]);
        }
    }
    return 1;
}

int get_line(char *buff, int lim) {
    int i, c;
    for (i = 0; i < lim && (c = getchar()) != EOF && c != '\n'; ++i)
        buff[i] = c;
    buff[i] = '\0';
    while (c != EOF && c != '\n')
        c = getchar();
        // printf("oops");
            ;
    return i;
}
