#include <stdio.h>

void back_escape(char *sourse, char *res) {
    unsigned i, j;
    for (i = j = 0; sourse[i] != '\0'; ++i, ++j) {
        if (sourse[i] == '\t' || sourse[i] == '\n') {
            res[j++] = '\\';
            switch (sourse[i]) {
            case '\t':
                res[j] = 't';
                break;
            case '\n':
                res[j] = 'n';
                break;
            }
        } else {
            res[j] = sourse[i];
        }
    }
    res[j] = '\0';
}

void escape(char *source) {
    unsigned i, j;
    for (i = j = 0; source[i] != '\0'; ++i, ++j) {
        if (source[i] == '\\') {
            switch (source[i + 1]) {
                case 't':
                    source[j] = '\t';
                    ++i;
                    break;
                case 'n':
                    source[j] = '\n';
                    ++i;
                    break;
                default:
                    source[j] = '\\';
                    continue;
            }
        } else {
            source[j] = source[i];
        }
    }
    source[j] = '\0';
}

int main(void) {
    char source[] = "\\hello\nworld\toops";
    char res[100];
    back_escape(source, res);
    escape(res);
    printf("%s", res);
}
