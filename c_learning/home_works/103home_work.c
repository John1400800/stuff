#include <stdio.h>
#include <math.h>
#include <stdlib.h>

#ifndef isdigit
#define isdigit(c) ((c) >= '0' && (c) <= '9')
#endif
#ifndef isspace
#define isspace(c) (((c)>9 && (c)<=13) || (c)==32)
#endif

#define round(n, accur) ((double)(int)((n)*pow(10, (accur)))/pow(10, accur))
#define frand(low, high) ((low)+(double)rand()/RAND_MAX*((high)-(low)))
#define init_arr(arr, size, acur, low, high)                                   \
    do {                                                                       \
        int i;                                                                 \
        for (i = 0; i < (size); ++i)                                           \
            arr[i] = round(frand((low), (high)), 2);                           \
    } while (0)

#define print_farr(arr, size, accur)                                           \
    do {                                                                       \
        int i;                                                                 \
        printf(#arr ":\n");                                                    \
        for (i = 0; i < (size); ++i)                                           \
            printf(i == (size)-1 ? "% ." #accur "lf\n" : "% ." #accur "lf, ",  \
                   arr[i]);                                                    \
    } while (0)

#define new(T, size) ((T *)malloc(sizeof(T)*(size)))

int sget_int(char *start_msg, char *repeat_msg);
int get_int(int *res);

int main(void) {
    int k;
    double arrx_size, *arrx, *arry, sq_sum;
    arrx =
        new (double, arrx_size = sget_int(
                         "enter num: ",
                         "try again: ")); // inp len arr and mem alloc for arrx
    init_arr(arrx, arrx_size, 2, -9.9, 9.9); // init arr x

    arry = new (double, arrx_size/2-1); // mem alloc for arry
    for (sq_sum = k = 0; k < arrx_size/2-1; ++k) {
        arry[k] = arrx[2*k]*arrx[2*k+1];
        sq_sum+=arry[k]*arry[k];
    }
    print_farr(arrx, arrx_size, 2);
    print_farr(arry, arrx_size/2-1, 2);
    printf("sq summ: %lf\n", sq_sum);
    return 0;
}

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
