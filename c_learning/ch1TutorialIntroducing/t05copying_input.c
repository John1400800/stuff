// 2 examples of input verification

#include <stdio.h>

int main() {
    char c;
    do                                  
        c = getchar();                  // the first way
    while (c != EOF && putchar(c));

    while ((c = getchar()) != EOF)      // and second way
        putchar(c);                     // maybe the second way is clearer

    for (int i = 32; i <= 126/2; ++i)   // print ascii table :)
        printf("%c\t%c\n", i, i+126/2);
}
