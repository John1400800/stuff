#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define ARR_SIZE 20

void print_arr(unsigned *arr, unsigned size) {
    if (size) {
        unsigned i;
        printf("{ ");
        for (i = 0; i < size; ++i) {
            printf("%d%s ", arr[i], i != size - 1 ? "," : "");
        }
        printf("}");
    } else {
        printf(" None");
    }
    putchar('\n');
}

int main(void) {
    unsigned i, arr[ARR_SIZE];
    unsigned m_5, m_7, j, mult_5[ARR_SIZE], mult_7[ARR_SIZE], other[ARR_SIZE];
    srand((unsigned)time(NULL));
    printf("initial array: %-17s{ ", "");
    for (i = 0; i < ARR_SIZE; ++i) {
        arr[i] = (unsigned)rand() % 100 + 1;
        printf("%d%s ", arr[i], i != ARR_SIZE - 1 ? "," : "");
    }
    printf("}\n");
    for (i = j = m_5 = m_7 = 0; i < ARR_SIZE; ++i) {
        if (arr[i] % 5 == 0) {
            mult_5[m_5++] = arr[i];
        } else if (arr[i] % 7 == 0) {
            mult_7[m_7++] = arr[i];
        } else {
            other[j++] = arr[i];
        }
    }
    printf("the numbers are multiples of 5: ");
    print_arr(mult_5, m_5);
    printf("the numbers are multiples of 7: ");
    print_arr(mult_7, m_7);
    printf("others: %-24s", "");
    print_arr(other, j);
	return 0;
}
