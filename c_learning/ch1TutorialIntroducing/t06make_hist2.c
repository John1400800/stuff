#include <stdio.h>

#define MAXLENGTH 100
#define isspace(c) (c)==' '||(unsigned)(c)-'\t'<5

int digits(int n);

int main(void) {
    int c, i, inword, curr_len, max_cnt, max_len, wlen_cnt[MAXLENGTH+1]={0};
    for (inword=0, curr_len=max_len=max_cnt=0; (c=getchar())!=EOF; ++curr_len)
        if (isspace(c)) {
            if (inword && curr_len<=MAXLENGTH) {
                if (curr_len>max_len)
                    max_len=curr_len;
                if (++wlen_cnt[curr_len] > max_cnt)
                    max_cnt=wlen_cnt[curr_len];
            }
            inword=0;
        } else if (!inword) {
            curr_len=0;
            inword=1;
        }
    max_len = digits(max_len);
    for (curr_len=1; curr_len<=MAXLENGTH; ++curr_len)
        if (wlen_cnt[curr_len]!=0) {
            printf("%*d: [", max_len, curr_len);
            for (i=0; i<wlen_cnt[curr_len]; ++i)
                putchar('|');
            printf("%*s]\n", max_cnt-wlen_cnt[curr_len], "");
        }
    return 0;
}

int digits(int n) {
    int digcnt=0;
    do
        ++digcnt;
    while ((n/=10)>0);
    return digcnt;
}
