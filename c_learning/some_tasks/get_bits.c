#include <stdio.h>
#include <stdlib.h>

int cnt_base_digts(unsigned num, unsigned base);
char *utoa(unsigned num, unsigned base, char *buffs);
#define utoa(num, base, buffs) (*utoa((num), (base), (buffs)) = '\0') 
unsigned getbits(unsigned bits, unsigned startidx, unsigned shiftwidth);

int main(void) {
    char *sp = (char *)malloc(sizeof(char)*10);
    unsigned orig_num = 0b100110101;
    unsigned res_num = getbits(orig_num, 2, 4);
    int cnt_dig_diff = cnt_base_digts(orig_num, 2) - cnt_base_digts(res_num, 2);
    cnt_dig_diff = cnt_dig_diff > 0? cnt_dig_diff : 0;

    utoa(orig_num, 2, sp);
    printf("%s\n", sp);
    while (cnt_dig_diff--)
        putc('0', stdout);
    utoa(res_num, 2, sp);
    printf("%s\n", sp);

    return 0;
}

int cnt_base_digts(unsigned n, unsigned b) {
    int cnt_digts = 1;
    while (n /= b)
        ++cnt_digts;
    return cnt_digts;
}

#undef utoa
char *utoa(unsigned n, unsigned b, char *buff) {
    if (n / b)
        buff = utoa(n / b, b, buff);
    *buff = '0' + n % b;
    return ++buff;
}

unsigned getbits(unsigned bits, unsigned startidx, unsigned shiftwidth) {
    return bits & (~(~0 << shiftwidth) << startidx);
}

