#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>
#include <stdio.h>

#define BUFFSIZE 2048
typedef enum exitStatus {
    SUCCESS = 0,
    FAILURE = 1
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

#define FILENAME "input.txt"
#define SEARCH_LETTER 't'

int main(void) {
    char text[BUFFSIZE];
    if (readText(text, FILENAME) == SUCCESS) {
        printf("Source text from file %s:\n%s\n", FILENAME, text);
        printf("The character '%c' appears %zu times.\n",
               SEARCH_LETTER, countOccurrences(text, SEARCH_LETTER));
    } else {
        printf("Failed to read text from the file.\n");
    }
    return EXIT_SUCCESS;
}
