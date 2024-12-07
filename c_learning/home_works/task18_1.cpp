#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <stdio.h>

#define MAX_LINE_LENGTH 1024
#define FILENAME "input.txt"

typedef struct {
    char **lines;
    size_t numLines;
    size_t maxLines;
} TextLines;

bool readTextFromFile(TextLines *lines, FILE *file) {
    if (lines->numLines == 0) {
        lines->maxLines = 10;
        lines->lines = malloc(lines->maxLines * sizeof(char*));
    }
    if (!lines->lines)
        return false;
    char buffer[MAX_LINE_LENGTH];
    while (fgets(buffer, sizeof(buffer), file)) {
        if (lines->numLines >= lines->maxLines) {
            size_t newMaxLines = lines->maxLines * 2;
            char **newLines = realloc(lines->lines, newMaxLines * sizeof(char*));
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

int main(void) {
    FILE *file = fopen(FILENAME, "r");
    if (!file) {
        fprintf(stderr, "Could not open file %s\n", FILENAME);
        return EXIT_FAILURE;
    }
    TextLines lines = {.numLines = 0};
    readTextFromFile(&lines, file);
    if (readTextFromFile(&lines, file)) {
        for (size_t i = 0; i < lines.numLines; ++i)
            printf("%zu: %s\n", i, lines.lines[i]);
        printf("the character 'l' occurs %zu times\n", countOccurrences(&lines, 'l'));
    } else
        fprintf(stderr, "Error reading from file\n");
    fclose(file);
    freeTextLines(&lines);
    return EXIT_SUCCESS;
}
