#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

// #define FILENAME "input.txt"
#define MAX_LINE_LENGTH 1024

typedef struct {
    char **lines; // dynamic array of 'char*' - lines
    size_t numLines;
    size_t maxLines;
} TextLines;

bool readTextFromFile(TextLines *lines, FILE *file) {
    if (!lines->lines) {
        lines->numLines = 0;
        lines->maxLines = 10;
        lines->lines = malloc(lines->maxLines * sizeof(char *));
    }
    if (!lines->lines)
        return false;
    char buffer[MAX_LINE_LENGTH];
    while (fgets(buffer, sizeof(buffer), file)) {
        if (lines->numLines >= lines->maxLines) {
            size_t newMaxLines = lines->maxLines * 2;
            char **newLines = realloc(lines->lines, newMaxLines * sizeof(char *));
            if (!newLines) {
                free(lines->lines);
                return false;
            }
            lines->lines = newLines;
            lines->maxLines = newMaxLines;
        }
        buffer[strcspn(buffer, "\n")] = '\0';
        lines->lines[lines->numLines] = strdup(buffer);
        if (!lines->lines[lines->numLines]) {
            free(lines->lines);
            return false;
        }
        ++lines->numLines;
    }
    return true;
}

size_t countOccurrences(const TextLines *lines, char searchChar) {
    size_t count = 0;
    for (size_t i = 0; i < lines->numLines; ++i)
        for (size_t j = 0; j < strlen(lines->lines[i]); ++j)
            if (lines->lines[i][j] == searchChar)
                ++count;
    return count;
}

void freeTextLines(TextLines *lines) {
    for (size_t i = 0; i < lines->numLines; ++i)
        free(lines->lines[i]);
    free(lines->lines);
    lines->lines = NULL;
    lines->numLines = lines->maxLines = 0;
}

void printTextLines(const TextLines *lines) {
    for (size_t i = 0; i < lines->numLines; ++i)
        printf("%zu: %s\n", i, lines->lines[i]);
}

int main(void) {
#ifndef FILENAME
    printf("Enter the name of the file to read: ");
    char filename[256];
    if (!fgets(filename, sizeof(filename), stdin)) {
        fprintf(stderr, "Error reading file name\n");
        return EXIT_FAILURE;
    }
    filename[strcspn(filename, "\n")] = '\0';
    FILE *file = fopen(filename, "r");
#else
    const char *filename = FILENAME;
    FILE *file = fopen(FILENAME, "r");
#endif
    if (!file) {
        fprintf(stderr, "Could not open file %s\n", filename);
        return EXIT_FAILURE;
    }
    TextLines lines = { NULL };
    if (readTextFromFile(&lines, file)) {
        printTextLines(&lines);
        printf("Enter a character to count occurrences of: ");
        char searchChar;
        if (scanf(" %c", &searchChar) != 1) {
            fprintf(stderr, "Error reading character\n");
            return EXIT_FAILURE;
        }
        printf("the character '%c' occurs %zu times\n", searchChar,
               countOccurrences(&lines, searchChar));
    } else {
        fprintf(stderr, "Error reading from file\n");
    }
    fclose(file);
    freeTextLines(&lines);
    return EXIT_SUCCESS;
}
