#include <stdlib.h>
#include <stdint.h>
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>

#define BUFFSIZE 2048
typedef enum exitStatus {
    FAILURE = 0,
    SUCCESS = 1
} exitStatus;

bool readText(char *text, const char* fileName) {
    FILE *file = fopen(fileName, "r");
    if (!file) {
        perror("\nFile open error\n");
        return FAILURE;
    }
    char ch;
    size_t i=0;
    while (i < BUFFSIZE-1 && (ch = fgetc(file)) != '*' && ch != EOF)
        text[i++] = ch;
    text[i] = '\0';
    fclose(file);
    return SUCCESS;
}

size_t countOccurrences(char *text, char searchChar) {
    size_t count=0;
    for (size_t i=0; i<BUFFSIZE-1 && text[i]!='\0' && text[i]!=EOF; ++i)
        if (text[i] == searchChar)
            ++count;
    return count;

}
#ifndef isspace
#define isspace(c) (((c) >= 9 && (c) <= 13) || (c) == 32)
#endif

void wrap_str(char *start_linep, int lim) {
    int islastspaces = 0;
    char *curr_posp;
    for (curr_posp = start_linep; *curr_posp != '\0'; ++curr_posp) {
        if (isspace(*curr_posp))
            islastspaces = 1;
        if (curr_posp - start_linep >= lim && islastspaces) {
            while (!isspace(*curr_posp))
                --curr_posp;
            *curr_posp++ = '\n';
            start_linep = curr_posp;
            islastspaces = 0;
        }
    }
}

#define FILENAME "input.txt"
#define SEARCH_LETTER 't'

int main(void) {
    char text[BUFFSIZE];
    if (readText(text, FILENAME)) {
        wrap_str(text, 30);
        printf("Source text from file %s:\n%s\n", FILENAME, text);
        printf("The character '%c' appears %zu times.\n",
               SEARCH_LETTER, countOccurrences(text, SEARCH_LETTER));
    } else {
        printf("Failed to read text from the file.\n");
    }
    return EXIT_SUCCESS;
}
