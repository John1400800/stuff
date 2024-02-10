#include <stdio.h>
#include <time.h>
#include <stdlib.h> 

typedef enum {CHAR, INT, FLOAT, DOUBLE} Type;

#ifndef NULL
#define NULL ((void *)0)
#endif

#define frand(low, high) ((low)+(double)rand()/RAND_MAX*((high)-(low)))
#define init_arr(arr, size, low, high)                                         \
    do {                                                                       \
        int i;                                                                 \
        for (i=0; i<(size); ++i)                                               \
            (arr)[i] = rand()%2 ? frand((low),(high)) : 0;                     \
    } while (0)

#define print_farr(arr, size)                                                  \
    do {                                                                       \
        int i;                                                                 \
        printf(#arr ":\n");                                                    \
        for (i = 0; i < (size); ++i)                                           \
            printf(i == (size)-1 ? "% .1lf\n" : "% .1lf, ", arr[i]);           \
    } while (0)

#define swap(T, a, b)                                                          \
    do {                                                                       \
        T temp = (a);                                                          \
        (a) = (b);                                                             \
        (b) = temp;                                                            \
    } while (0)

#define mv_zero_to_end(T, arr, arr_size)                                       \
    do {                                                                       \
        int i, j;                                                              \
        for (j = 1; j < (arr_size); ++j)                                       \
            for (i = 0; i < (arr_size)-j; ++i)                                 \
                if ((arr)[i] == 0)                                             \
                    swap(T, (arr)[i], (arr)[i + 1]);                           \
    } while (0)

#define new(T, size) (T *)alloc(sizeof(T)*(size)) /*syntax sugar*/

#define ARR_SIZE 10

void *alloc(int n);
void free(void *ptr);
void *find_max_abs(Type type, void *arr, int arr_size);

int main(void) {
    int i;
    double *arr = new (double, ARR_SIZE);           // mem alloc
    srand(time(NULL));                              // rand func init
    init_arr(arr, ARR_SIZE, -9.9, 9.9);
    mv_zero_to_end(double, arr, ARR_SIZE);
    printf("arr:\n");
    print_arr(arr, ARR_SIZE);
    printf("abs max:\n%.1lf\n",
           *(double *)find_max_abs(DOUBLE, arr, ARR_SIZE)); // primt abs max
    return 0;
}

#define abs(a) ((a) < 0 ? -(a) : (a))
#define macro(T, arrptr, maxptr)                                               \
    do {                                                                       \
        int i;                                                                 \
        for (maxptr = arrptr, i = 1; i < arr_size; ++i)                        \
            if (abs(*((T *)arrptr + i)) > abs(*(T *)maxptr))                   \
                maxptr = (T *)arrptr + i;                                      \
    } while (0)

// TODO: return this function to its normal appearance
void *find_max_abs(Type type, void *arr, int arr_size) {
    void *max;
    switch (type) {
    case CHAR:
        macro(char, arr, max);
        break;
    case INT:
        macro(int, arr, max);
        break;
    case FLOAT:
        macro(float, arr, max);
        break;
    case DOUBLE:
        macro(double, arr, max);
        break;
    }
    return max;
}
#undef macro

#define ALLOCSIZE 1000

static char allocbuff[ALLOCSIZE];
static char *allocp = allocbuff;

void *alloc(int n) {
    return (allocp + n <= allocbuff + ALLOCSIZE) ? (allocp+=n)-n : NULL;
}

void free(void *ptr) {
    if ((char *)ptr >= allocbuff && (char *)ptr < allocbuff + ALLOCSIZE)
        allocp = (char*)ptr;
    else
        printf("free: out of allocbuff");
}
