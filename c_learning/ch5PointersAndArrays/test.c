#include <stdio.h>

void swap(int *px, int *py) {
    int temp;
    temp = *px;
    *px = *py;
    *py = temp;
}

int main(void) {
    int x, y;
    x = 1;
    y = 2;
    swap(&x, &y);
    printf("x=%d, y=%d", x, y);
    return 0;
}
