#include <stdio.h>

void swap_(int *a, int *b) {
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
}

int main(void) {
    int x = 1, y = 2;
    swap_(&x, &y);
    printf("%d, %d", x, y);
    return 0;
}
