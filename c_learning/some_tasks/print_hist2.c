#include <ctype.h>
#include <stdio.h>


#define MAX_LENGTH 1000

int cnt_digits(unsigned num) {
    int cnt = 1;
    while ((num /= 10) > 0)
        ++cnt;
    return cnt;
}

void print_hist(unsigned *hist) {
    unsigned i;
    int spaces;
    printf("length: ");
    for (i = 1; i < hist[0]; ++i) {
        if (hist[i] > 0) {
            spaces = cnt_digits(hist[i]) - cnt_digits(i);
            spaces = spaces > 0 ? spaces : 0;
            while (spaces-- > 0) {
                putchar(' ');
            }
            printf("%d ", i);
        }
    }
    putchar('\n');
    printf("count:  ");
    for (i = 1; i < hist[0]; ++i) {
        if (hist[i] > 0) {
            spaces = cnt_digits(i) - cnt_digits(hist[i]);
            spaces = spaces > 0 ? spaces : 0;
            while (spaces-- > 0) {
                putchar(' ');
            }
            printf("%d ", hist[i]);
        }
    }
}

void make_hist(char *s, unsigned *hist) {
    int i = 0;
    int islastspace = 1;
    int curr_length = 0;
    while (s[i] != '\0') {
        if (!isspace(s[i])) {
            ++curr_length;
            islastspace = 0;
        } else if (!islastspace) {
            ++hist[curr_length];
            curr_length = 0;
            islastspace = 1;
        }
        ++i;
    }
    ++hist[curr_length];
}

int main() {
    unsigned hist[MAX_LENGTH + 1] = {0};
    hist[0] = MAX_LENGTH;

    char s[] = "**************** **** *** *"
               " ****** * *************"
               " ******** ** *********** ****"
               " ** ***** *** ******** ***"
               " ****** * ****** *** **"
               " ****** * * * *** *****";
    make_hist(s, hist);
    print_hist(hist);
    // printf("%d", cnt_digits(12));
}
