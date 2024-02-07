#include <stdio.h>
#include <stdlib.h>

#define SIZE 7
#define rrand(low, high) ((low) + rand() % ((high) - (low) + 1))

int *generate(int size);
int search_lonely(int *arr, int size);
int search_lonely2(int *arr, int size);

int main(void) {
    int i, *arr;
    for(;;) {
        arr = generate(SIZE);
        for (i = 0; i < SIZE; ++i)
            printf("%d ", arr[i]);
        putchar(':');
        printf(" %d\n", search_lonely2(arr, SIZE));
    }
}

int *generate(int size) {
    int i, j, r;
    int *res = malloc(sizeof(int) * size + 1);
    for (i = 0; i < size + 1; ++i)
        res[i] = 0;
    for (i = 0; i < size; ++i) {
        if (res[i])
            continue;
        res[i] = r = rrand(1, 9);
        do {
            j = rrand(i + 1, size);
        } while (res[j]);
        res[j] = r;
    }
    return res;
}

int search_lonely(int *arr, int size) {
    int i, j, k;
    int *lonely = (int *)malloc(sizeof(int) * size / 2 + 1);
    for (j = 0; j < size; ++j)
        lonely[j] = 0;
    for (i = 0, k = 0; i < size; ++i) {
        for (j = 0; j < k; ++j)
            if (arr[i] == lonely[j]) {
                lonely[j] = 0;
                break;
            }
        if (j == k)
            lonely[k++] = arr[i];
    }
    while (--k >= 0)
        if (lonely[k])
            return lonely[k];
    return 0;
}

int search_lonely2(int *arr, int size) {
    unsigned i, lonely = 0;
    for (i = 0; i < size; ++i)
        lonely ^= arr[i];
    return lonely;
}
