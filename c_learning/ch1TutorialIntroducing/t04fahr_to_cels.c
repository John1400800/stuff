#include <stdio.h>

#define LOWER 0
#define UPPER 300
#define STEP  20

int main() {
	printf("cels fahr\n");
    for (int cels = LOWER; cels <= UPPER; cels += STEP) {
        printf("%4d %4d\n", cels, 9 * cels / 5 + 32);
    }
}
