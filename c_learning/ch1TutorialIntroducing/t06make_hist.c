#include <ctype.h>
#include <stdio.h>

#define MAX_LENGTH 100

static const char digit[] = "0123456789abcdef";

// добавляем в индекс длины в hist кол-во слов этой длины
void make_hist(char s[], int hist[], int max_length) {
    int idx = 0;
    int last_is_space = 1;
    int curr_length = 0;
    while (s[idx] != '\0') {
        if (!isspace(s[idx])) {
            last_is_space = 0;
            ++curr_length;
        } else if (!last_is_space) {
            last_is_space = 1;
            if (curr_length <= max_length) {
                ++hist[curr_length];
            }
            curr_length = 0;
        }
        ++idx;
    }
    if (curr_length <= max_length) {
        ++hist[curr_length];
    }
}

int len_str(char source[]) {
    int curr_pos = 0;
    while (source[curr_pos] != '\0') {
        ++curr_pos;
    }
    return curr_pos;
}

void reverse(char source[]) {
    char buff;
    int low = 0;
    int high = len_str(source) - 1;
    while (low < high) {
        buff = source[low];
        source[low] = source[high];
        source[high] = buff;
        ++low;
        --high;
    }
}

void itoa(int num, char res_num[]) {
    int curr_pos = 0;
    int minus = num < 0 ? num *= -1, 1 : 0;
    do {
        res_num[curr_pos++] = digit[num % 10];
    } while ((num /= 10) > 0);
    if (minus) {
        res_num[curr_pos++] = '-';
    }
    res_num[curr_pos] = '\0';
    reverse(res_num);
}

int cnt_digits(int n) {
    int dgts = 1;
    while ((n /= 10) > 0) {
        ++dgts;
    }
    return dgts;
}

void print_num(int num) {
    static char snum[100];
    itoa(num, snum);
    for (int cr_pos = 0; snum[cr_pos] != '\0'; ++cr_pos) {
        putchar(snum[cr_pos]);
    }
}

// much slower than hprinthist but ...
void vprinthist(int hist[], int max_length) {
    int curr_length = 0;
    int is_cntn = 1;
    int curr_lvl = 1; // >= lvl
    int spaces;
    for (curr_length = 1; curr_length <= max_length; ++curr_length) {
        if (hist[curr_length]) {
            print_num(curr_length);
            putchar(' ');
        }
    }
    putchar('\n');
    while (is_cntn) {
        is_cntn = 0;
        for (curr_length = 1; curr_length <= max_length; ++curr_length) {
            if (hist[curr_length]) {
                for (spaces = cnt_digits(curr_length) - 1; spaces > 0;
                     --spaces) {
                    putchar(' ');
                }
                if (hist[curr_length] >= curr_lvl) {
                    putchar('*');
                    is_cntn = 1;
                } else {
                    putchar(' ');
                }
                putchar(' ');
            }
        }
        putchar('\n');
        ++curr_lvl;
    }
}

void hprinthist(int hist[], int max_length) {
    int i, j;
    for (i = 1; i <= max_length; ++i) {
        if (hist[i]) {
            putchar('0' + i);
            putchar(':');
            putchar(' ');
            for (j = hist[i]; j > 0; --j) {
                putchar('*');
            }
            putchar('\n');
        }
    }
}

int get_str(char buff_str[], int lim) {
    int idx = 0;
    while (idx < lim && (buff_str[idx] = (char)getchar()) != EOF &&
           !(idx > 0 && buff_str[idx] == '\n' && buff_str[idx - 1] == '\n')) {
        ++idx;
    }
    buff_str[idx] = '\0';
    return idx;
}

int main() {
    int hist[MAX_LENGTH + 1] = {0};
    char s[MAX_LENGTH + 1];
    get_str(s, MAX_LENGTH);
    make_hist(s, hist, MAX_LENGTH);
    vprinthist(hist, MAX_LENGTH);
}
