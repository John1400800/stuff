#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define LINE_LEN 20
#define MAX_LINES 100

typedef char Line[LINE_LEN];
Line Text[MAX_LINES];

int countOccurrences(Line text[], char symbol) {
    int count = 0;
    for (int i = 0; i < MAX_LINES; ++i) {
        for (int j = 0; j < LINE_LEN; ++j) {
            if (text[i][j] == symbol) {
                count++;
            }
        }
    }
    return count;
}

void readText(Line text[], const char* filename) {
    FILE* file = fopen(filename, "r");
    if (!file) {
        perror("File open error");
        exit(EXIT_FAILURE);
    }

    int lineIdx = 0;
    int charIdx = 0;
    char ch;

    while ((ch = fgetc(file)) != '*' && ch != EOF) {
        text[lineIdx][charIdx] = ch;
        charIdx++;

        if (charIdx == LINE_LEN) {
            lineIdx++;
            if (lineIdx >= MAX_LINES) break;
            charIdx = 0;
        }
    }

    while (charIdx < LINE_LEN) {
        text[lineIdx][charIdx] = ' ';
        charIdx++;
    }

    fclose(file);
}

void printText(Line text[]) {
    for (int i = 0; i < MAX_LINES; ++i) {
        printf("%.*s\n", LINE_LEN, text[i]);
    }
}

int main() {
    readText(Text, "input.txt");

    printf("Text:\n");
    printText(Text);

    char target = 'e';
    int totalCount = countOccurrences(Text, target);
    printf("Character '%c' appears %d time(s)\n", target, totalCount);

    return EXIT_SUCCESS;
}
