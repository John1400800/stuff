#include <stddef.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define BUFFER_SIZE 1024
#define MAX_LINE_LENGTH 3

typedef struct {
    char **lines; // dynamic array of 'char*' - lines
    size_t numLines;
    size_t maxLines;
} TextLines;

void freeTextLines(TextLines *lines);

bool readTextFromFile(TextLines *lines, FILE *file, size_t maxLineLength) {
    if (!lines->lines) {
        lines->numLines = 0;
        lines->maxLines = 10;
        lines->lines = malloc(lines->maxLines * sizeof(char *));
    }
    if (!lines->lines)
        return false;

    char buffer[BUFFER_SIZE];
    while (fgets(buffer, sizeof(buffer), file)) {
        size_t len = strlen(buffer);
        buffer[strcspn(buffer, "\n")] = '\0';

        size_t start = 0;
        while (start < len) {
            size_t end = start + maxLineLength;
            if (end >= len) {
                end = len;
            } else {
                size_t spacePos = end;
                while (spacePos > start && buffer[spacePos] != ' ') {
                    --spacePos;
                }
                if (spacePos > start) {
                    end = spacePos;
                }
            }

            size_t chunkLength = end - start;
            char *lineChunk = malloc(chunkLength + 1);
            if (!lineChunk) {
                freeTextLines(lines);
                return false;
            }
            strncpy(lineChunk, buffer + start, chunkLength);
            lineChunk[chunkLength] = '\0';

            if (lines->numLines >= lines->maxLines) {
                size_t newMaxLines = lines->maxLines * 2;
                char **newLines = realloc(lines->lines, newMaxLines * sizeof(char *));
                if (!newLines) {
                    freeTextLines(lines);
                    return false;
                }
                lines->lines = newLines;
                lines->maxLines = newMaxLines;
            }

            lines->lines[lines->numLines] = lineChunk;
            ++lines->numLines;

            start = end;
            while (start < len && buffer[start] == ' ') {
                ++start;
            }
        }
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

int32_t main(int32_t argc, const char **argv) {
    char filename[256];
    char searchChar;
    if (argc >= 2) {
        strcpy(filename, argv[1]);
    } else {
        printf("Enter the name of the file to read: ");
        if (!fgets(filename, sizeof(filename), stdin)) {
            fprintf(stderr, "Error reading file name\n");
            return EXIT_FAILURE;
        }
        filename[strcspn(filename, "\n")] = '\0';
    }
    FILE *file = fopen(filename, "r");
    if (!file) {
        fprintf(stderr, "Could not open file %s\n", filename);
        return EXIT_FAILURE;
    }
    TextLines lines = { NULL };
    if (readTextFromFile(&lines, file, MAX_LINE_LENGTH)) {
        printTextLines(&lines);
        if (argc == 3) {
            searchChar = argv[2][0];
        } else {
            printf("Enter a character to count occurrences of: ");
            if (scanf(" %c", &searchChar) != 1) {
                fprintf(stderr, "Error reading character\n");
                return EXIT_FAILURE;
            }
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
