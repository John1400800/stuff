#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define max(a, b)   ({ __typeof__ (a) _a = (a), _b = (b); _a > _b ? _a : _b; })
#define MAXLINE     100
#define NUM_HEADERS 6

typedef struct {
    char *processor;
    char *ram_size;
    char *graphics_adapter;
    char *disk_space;
    char *wifi_interface;
} Column;

static const char *headers[] = {
    "numer",
    "processor",
    "ram size",
    "graphics adapter",
    "disk space",
    "wifi interface",
};

char *ultoa(size_t n, char s[]);
char *rtrim(char *str);

int main(void) {
    size_t i, j, num_of_rows, columns_size[6];
    char buffs[MAXLINE];
    /*** Init Table ***/
    for (i = 0; i < NUM_HEADERS; ++i)
        columns_size[i] = strlen(headers[i]);
    printf("Enter number of lines:\n");
    Column *rows=malloc(sizeof(Column)*(num_of_rows = strtoul(fgets(buffs, MAXLINE, stdin), NULL, 10)));
    columns_size[0] = max(columns_size[0], strlen(ultoa(num_of_rows, buffs)));
    for (i = 0; i < num_of_rows; ++i) {
        printf("desktop %ld\nEnter the processor model:\n", i+1);
        rtrim(fgets(buffs, MAXLINE, stdin));
        strcpy(rows[i].processor=malloc(sizeof(char)*(strlen(buffs)+1)), buffs);
        printf("Enter the ram size:\n");
        rtrim(fgets(buffs, MAXLINE, stdin));
        strcpy(rows[i].ram_size=malloc(sizeof(char)*(strlen(buffs)+1)), buffs);
        printf("Enter the graphics adapter:\n");
        rtrim(fgets(buffs, MAXLINE, stdin));
        strcpy(rows[i].graphics_adapter=malloc(sizeof(char)*(strlen(buffs)+1)), buffs);
        printf("Enter the disk space:\n");
        rtrim(fgets(buffs, MAXLINE, stdin));
        strcpy(rows[i].disk_space=malloc(sizeof(char)*(strlen(buffs)+1)), buffs);
        printf("Enter the wifi interface:\n");
        rtrim(fgets(buffs, MAXLINE, stdin));
        strcpy(rows[i].wifi_interface=malloc(sizeof(char)*(strlen(buffs)+1)), buffs);
        columns_size[1] = max(columns_size[1],strlen(rows[i].processor));
        columns_size[2] = max(columns_size[2],strlen(rows[i].ram_size));
        columns_size[3] = max(columns_size[3],strlen(rows[i].graphics_adapter));
        columns_size[4] = max(columns_size[4],strlen(rows[i].disk_space));
        columns_size[5] = max(columns_size[5],strlen(rows[i].wifi_interface));
    }
    /*** Draw Table ***/
    for (i = 0; i < NUM_HEADERS; ++i) {
        putchar('+');
        for (j = 0; j < columns_size[i]+2; ++j)
            putchar('=');
    }
    printf("+\n");
    for (i = 0; i < NUM_HEADERS; ++i)
        printf("| %-*s", (int)columns_size[i]+1, headers[i]);
    printf("|\n");
    for (i = 0; i < NUM_HEADERS; ++i) {
        putchar('+');
        for (j = 0; j < columns_size[i]+2; ++j)
            putchar('=');
    }
    printf("+\n");
    for (i = 0; i < num_of_rows; ++i)
        printf("| %-*ld| %-*s| %-*s| %-*s| %-*s| %-*s|\n",
                (int)columns_size[0]+1, i+1,
                (int)columns_size[1]+1, rows[i].processor,
                (int)columns_size[2]+1, rows[i].ram_size,
                (int)columns_size[3]+1, rows[i].graphics_adapter,
                (int)columns_size[4]+1, rows[i].disk_space,
                (int)columns_size[5]+1, rows[i].wifi_interface);
    for (i = 0; i < NUM_HEADERS; ++i) {
        putchar('+');
        for (j = 0; j < columns_size[i]+2; ++j)
            putchar('=');
    }
    printf("+\n");
    return 0;
}

char *rtrim(char *str) {
    char *end=str+strlen(str)-1;
    while (end > str && isspace(*end))
        --end;
    end[1]='\0';
    return str;
}

void reverse(char s[]);

char *ultoa(size_t n, char s[]) {
    int i = 0;
    do
        s[i++] = (char)(n % 10) + '0';
    while ((n /= 10) > 0);
    s[i] = '\0';
    reverse(s);
    return s;
}

void reverse(char s[]) {
    size_t i, j;
    char c;
    for (i = 0, j = strlen(s)-1; i<j; i++, j--) {
        c = s[i];
        s[i] = s[j];
        s[j] = c;
    }
}
