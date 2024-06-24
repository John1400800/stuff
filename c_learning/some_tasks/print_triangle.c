#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

void printTriangle(uint8_t height);

int main(void) {
    printTriangle(30);
    return EXIT_SUCCESS;
}

void printTriangle(uint8_t height) {
    uint8_t level, stars, spaces;
    for (level = 1; level <= height; ++level) {
        for (spaces=height-level; spaces>0; --spaces)
            putchar(' ');
        for (stars=(uint8_t)(level*2-1); stars>0; --stars)
            putchar('*');
        putchar('\n');
    }
}
