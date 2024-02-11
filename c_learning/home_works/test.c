#include <stdio.h>
#include <math.h>
#include <time.h>
#include <stdlib.h> 

typedef enum {CHAR, INT, FLOAT, DOUBLE} Type;

#ifndef NULL
#define NULL ((void *)0)
#endif

#ifndef isdigit
#define isdigit(c) ((c) >= '0' && (c) <= '9')
#endif
#ifndef isspace
#define isspace(c) (((c)>9 && (c)<=13) || (c)==32)
#endif

#define floor(n, accur) ((double)(int)((n)*pow(10, (accur)))/pow(10, accur))
#define frand(low, high) ((low)+(double)rand()/RAND_MAX*((high)-(low)))
#define init_rfarr(arr, size, accur, low, high)                                \
    do {                                                                       \
        int i;                                                                 \
        for (i = 0; i < (size); ++i)                                           \
            arr[i] = floor(frand((low), (high)), accur);                       \
    } while (0)

#define print_farr(arr, size, accur)                                           \
    do {                                                                       \
        int i;                                                                 \
        printf(#arr ":\n");                                                    \
        for (i = 0; i < (size); ++i)                                           \
            printf(i == (size)-1 ? "% ." #accur "lf\n" : "% ." #accur "lf, ",  \
                   arr[i]);                                                    \
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

#ifdef _INC_STDLIB
#define ull unsigned long long
#define new(T, size) (T *)malloc(sizeof(T)*(ull)(size)) /*syntax sugar*/
#else
#define new(T, size) (T *)alloc((int)sizeof(T)*(size)) /*syntax sugar*/
#endif

#define ACCUR 2

void *alloc(int n);
void free(void *ptr);
void *find_max_abs(Type type, void *arr, int arr_size);
int sget_int(char *start_msg, char *repeat_msg);

int main(void) {
    int arr_size; // arr_size ->> n
    double *arr =
        new (double, (arr_size = sget_int("enter n: ", "try again"))); // mem alloc
    srand((unsigned)time(NULL)); // init rand func
    init_rfarr(arr, arr_size, ACCUR, -9.9, 9.9);
    mv_zero_to_end(double, arr, arr_size);
    print_farr(arr, arr_size, 2/*2->>ACCUR*/);
    printf("abs max:\n%.2lf\n",
           *(double *)find_max_abs(DOUBLE, arr, arr_size)); // primt abs max
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

int get_int(int *res) {
    int c, isdig, start, sign;
    sign = 0;
    c=getchar();
    if (c=='+'||c=='-') {
        sign=c=='-'?-1:1;
        c=getchar();
    }
    for (*res=0, isdig=start=1; c!='\n'; c=getchar()) {
        if (isdig && (isdig=isdigit(c)))
            *res=*res*10+c-'0';
        start=0;
    }
    *res *= *res ? (sign?sign:1) : 1;
    return !(sign==-1 && !*res) && isdig && !start;
}

int sget_int(char *start_msg, char *repeat_msg) {
    int res;
    printf("%s", start_msg);
    while (!get_int(&res))
        printf("%s", repeat_msg);
    return res;
}

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
