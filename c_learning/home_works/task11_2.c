// A1 = An - (n-1)*d
// 2, 5, 8, 11, 14
// 1, 2, 3,  4,  5
// (9-3)/(4-1) = 2

// #define comm_diff(_t1, _t2)                                                    \
//     (((_t2).num > (_t1).num)                                                   \
//          ? (((_t2).val - (_t1).val) / ((_t2).num - (_t1).num))                 \
//          : (((_t1).val - (_t2).val) / ((_t1).num - (_t2).num)))

// #define msum_of_nterms(_t1, _t2, _n)                                           \
//     ((2 * (_t1).val + (_n - 2 * (_t1).num + 1) * comm_diff(_t1, _t2)) * _n / 2)

#include <stdio.h>

#ifndef _INC_CTYPE
#define isdigit(c) ((c) > '0' && (c) < '9')
#endif
#define Arithmetic_sequence_term_init(_term)                                   \
    do {                                                                       \
        (_term).val = sget_int("enter value of " #_term ": ", AGNMSG);         \
        (_term).num = sget_int("enter number of " #_term ": ", AGNMSG);        \
    } while (0)

#define AGNMSG "try again"

typedef struct {
    unsigned num;
    int val;
} Arithmetic_sequence_term;

int sum_of_nterms(const Arithmetic_sequence_term *,
                  const Arithmetic_sequence_term *, unsigned);

int sget_int(char *start_msg, char *repeat_msg);

int main(void) {
    Arithmetic_sequence_term t1;
    Arithmetic_sequence_term t2;
    Arithmetic_sequence_term_init(t1);
    Arithmetic_sequence_term_init(t2);
    printf("%d",
           sum_of_nterms(&t2, &t1, sget_int("enter num of seq: ", AGNMSG)));
}

int sum_of_nterms(const Arithmetic_sequence_term *t1,
                  const Arithmetic_sequence_term *t2, unsigned n) {
    int comm_diff;
    comm_diff = (t1->num > t2->num) ? (t1->val - t2->val) / (t1->num - t2->num)
                                    : (t1->val - t2->val) / (t1->num - t2->num);
    return ((2 * t1->val + (n - 2 * t1->num + 1) * comm_diff) * n / 2);
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


