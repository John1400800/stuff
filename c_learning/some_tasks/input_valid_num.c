#include <stdio.h>

#define MAXLINE 100

int ascii_to_digit(char c) {
    switch (c) {
    case '0':
        return 0;
    case '1':
        return 1;
    case '2':
        return 2;
    case '3':
        return 3;
    case '4':
        return 4;
    case '5':
        return 5;
    case '6':
        return 6;
    case '7':
        return 7;
    case '8':
        return 8;
    case '9':
        return 9;
    default:
        return -1;
    }
}

int ascii_to_unsigned(char *ascii_array) {
    unsigned result, position;
    int curr_digit;
    result = 0;
    for (position = 0;
         (curr_digit = ascii_to_digit(ascii_array[position])) != -1;
         ++position) {
        result = result * 10 + (unsigned)curr_digit;
    }
    if (ascii_array[position] == '\0' && position != 0) {
        return (int)result;
    }
    return -1;
}

int is_negative(char *ascii_array) {
    return ascii_array[0] == '-' ? ascii_array[0] = '0', 1 : 0;
}

unsigned get_line(char *buff_ascii_array, unsigned lim) {
    unsigned position;
    for (position = 0; position < lim && (buff_ascii_array[position] = (char)getchar()) != '\n'; ++position) {
        ;
    }
    buff_ascii_array[position] = '\0';
    return position;
}

int input_valid_num(char *ascii_array, unsigned lim) {
    int is_neg, num;
    for (;;) {
        get_line(ascii_array, lim);
        is_neg = is_negative(ascii_array);
        num = ascii_to_unsigned(ascii_array);
        if (num != -1 && !(num == 0 && is_neg)) {
            break;
        }
        printf("try again: ");
    }
    return is_neg ? -num : num;
}

int main(void) {
    char s[MAXLINE + 1];
    printf("input number: ");
    printf("%d", input_valid_num(s, MAXLINE));
}
