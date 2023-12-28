#include <stdio.h>

#define MAXLINE 1000

unsigned str_copy(char *source, char *str_buff, unsigned i) {
	int j = 0;
	while ((str_buff[i] = source[j]) != '\0') {
		++i;
		++j;
	}
	return i;
}

unsigned get_line(char *buff_str, unsigned lim) {
    unsigned i = 0;
    while (i < lim - 1 && (buff_str[i] = (char)getchar()) != '\n') {
        ++i;
    }
    buff_str[i] = '\0';
    return i;
}

int lstr_index(char *source, char *sub) {
    int i, j;
    i = 0;
    while (source[i] != '\0') {
        j = 0;
        while (sub[j] != '\0' && source[i + j] != '\0' &&
               sub[j] == source[i + j]) {
            ++j;
        }
        if (sub[j] == '\0') {
            return i;
        }
        ++i;
    }
    return -1;
}

int main(void) {
	char res[MAXLINE*10];
	unsigned i = 0;
	char s[MAXLINE + 1];
	char sub_s[MAXLINE + 1];

	printf("input sub str: ");
	while (!get_line(sub_s, MAXLINE)) {
		printf("try again: ");
	}
	printf("input strings:\n");
	while(get_line(s, MAXLINE)) {
		if (lstr_index(s, sub_s) >= 0) {
			i = str_copy(s, res, i);
			i = str_copy("\n", res, i);
		}
	}
	if (i > 0) {
		printf("%s", res);
		return 0;
	} else {
		return 1;
	}
}
