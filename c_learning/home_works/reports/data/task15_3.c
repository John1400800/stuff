#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAXLINE 1024
#define DELIM ";"

char ***readrows(FILE *file, int *nrow, int *ncol);
char **strparce(const char *line, const char *delim, int *ncol);
void printrows(char ***rows, const long *col_len, int nrow, int ncol, int flag);
char ***search_in_rows(char ***rows, const char *smsg, int *snrow, int (*sfunc)(char**, const char*));
long *get_col_len(char ***rows, int nrow, int ncol);
static long rtrimlen(const char *s);

int match_by_num(char **row, const char *smsg);

int main(void) {
    char buffer[MAXLINE], ***rows, ***srows;
    int row, nrow, snrow, ncol;
    long *col_len;
    FILE *file;

    file = fopen("table2.csv", "r");
    rows = readrows(file, &nrow, &ncol);
    fclose(file);

    snrow = nrow;
    srows = search_in_rows(rows, strdup("120"), &snrow, match_by_num);
    col_len = get_col_len(rows, nrow, ncol);
    printrows(rows, col_len, 1, ncol, 1);
    printrows(srows, col_len, snrow, ncol, 0);
    return 0;
}

char **
strparce(const char *line, const char *delim, int *ncol) {
    int col;
    char *token, **row=NULL;
    if (*ncol!=0)
        row = (char**)malloc(*ncol*sizeof(char*));
    for (col=0, token=strtok(line, delim);
            token!=NULL;
            ++col, token=strtok(NULL, delim))
    {
        if (*ncol==0)
            row = (char**)realloc(row, (col+1)*sizeof(char*));
        else if (col>=*ncol)
            break;
        row[col] = strndup(token, rtrimlen(token));
    }
    if (*ncol==0)
        *ncol = col;
    return row;
}

char ***
readrows(FILE *file, int *nrow, int *ncol) {
    int col;
    char ***rows, *token, line[1024];
    rewind(file);
    for (*nrow=*ncol=0, rows=NULL;
            fgets(line, sizeof(line), file)!=NULL; // `feof` maybe crash
            ++*nrow)
    {
        rows = (char***)realloc(rows, (*nrow+1)*sizeof(char**));
        rows[*nrow] = strparce(line, DELIM, ncol);
    }
    if (*nrow==0)
        return NULL;
    return rows;
}


void
printrows(char ***rows, const long *col_len, int nrow, int ncol, int flag) {
    int i, j, k, n;
    for (i=n=0; i<nrow; ++i) {
        if (n<2&&flag) {
            for (j=0; j<ncol; ++j) {
                putchar('+');
                for (k=0; k<col_len[j]+2; ++k)
                    putchar('-');
            }
            printf("+\n");
            ++n;
        }
        for (j=0; j<ncol; ++j)
            printf("| %-*s", (int)col_len[j]+1, rows[i][j]);
        printf("|\n");
    }
    if (n<=2) {
        for (j=0; j<ncol; ++j) {
            putchar('+');
            for (k=0; k<col_len[j]+2; ++k)
                putchar('-');
        }
        printf("+\n");
    }
}

long *
get_col_len(char ***rows, int nrow, int ncol) {
    int i, j;
    long *col_len;
    col_len = (long*)malloc(ncol*sizeof(long));
    for (i=0; i<nrow; ++i)
        for (j=0; j<ncol; ++j) {
            if (i==0)
                col_len[j] = 0;
            if (strlen(rows[i][j]) > col_len[j])
                col_len[j] = strlen(rows[i][j]); 
        }
    return col_len;
}

char ***
search_in_rows(char ***rows, const char *smsg, int *snrow, int (*sfunc)(char**, const char*)) {
    char ***srows;
    int i, count;
    for (i=1, count=0, srows=NULL; i<*snrow; ++i) {
        if (sfunc(rows[i], smsg)) {
            srows = (char***)realloc(srows, (count+1)*sizeof(char**));
            srows[count] = rows[i];
            count++;
        }
    }
    *snrow = count;
    return srows;
}

int
match_by_num(char **row, const char *smsg) {
    return atoi(row[3])>=atoi(smsg);
}

long
rtrimlen(const char *s) {
    long len;
    for (len=(long)strlen(s)-1; len>=0 && isspace(s[len]); --len)
        ;
    return len+1;
}
