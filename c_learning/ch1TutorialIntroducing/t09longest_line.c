#include <stdio.h>

#define MAX_LENGTH 100

/* copies from str1 to str2 */
void cpy_str(char str1[], char str2[]) {
    int curr_pos = 0;
    while ((str2[curr_pos] = str1[curr_pos]) != '\0') {
        ++curr_pos;
    }
}

/* writes the input to str[]
and returns the length of the input */
int get_str(char str[], int lim) {
    int curr_pos = 0;
    while (
        curr_pos < lim && (str[curr_pos] = (char)getchar()) != EOF &&
        !(curr_pos > 0 && str[curr_pos - 1] == '\n' && str[curr_pos] == '\n'))
    {
        ++curr_pos;
    }
    str[curr_pos] = '\0';
    if (curr_pos == 1 && str[curr_pos - 1] == '\n' && str[curr_pos] == '\0') {
        return 0;
    } else {
        return curr_pos;
    }
}

int main() {
    char longest[MAX_LENGTH + 1];
    int longest_length = 0;
    char curr[MAX_LENGTH + 1];
    int curr_length;
    while ((curr_length = get_str(curr, MAX_LENGTH)) > 0) {
        if (curr_length > longest_length) {
            longest_length = curr_length;
            cpy_str(curr, longest);
        }
    }
    if (longest_length > 0) {
        printf("%s", longest);
        return 0;
    } else {
        printf("the longest string has a length of 0");
        return 1;
    }
}
