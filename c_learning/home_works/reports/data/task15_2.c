#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define DELIM ";"
#define MAXLINE 1024

enum {
    EXIT,
    DISPLAY, ADD, SEARCH1, SEARCH2
};

void writerows(FILE *file, char ***rows, int nrow, int ncol);
char ***readrows(FILE *file, int *nrow, int *ncol);
char **strparce(const char *line, const char *delim, int *ncol);
void printrows(char ***rows, const long *col_len, int nrow, int ncol, int flag);
char ***search_in_rows(char ***rows, const char *smsg, int *snrow, int (*sfunc)(char**, const char*));
long *get_col_len(char ***rows, int nrow, int ncol);
static long rtrimlen(const char *s);

int is_valid(const char *line, const char *delim);
static int is_valid_4num(const char *line);

int match_by_num(char **row, const char *smsg);
int match_by_mileage(char **row, const char *smsg);

int
main(void) {
    char buffer[MAXLINE], ***rows, ***srows;
    int is_continue, nrow, snrow, ncol;
    long *col_len;
    FILE *file;

    file = fopen("table1.csv", "r+");
    rows = readrows(file, &nrow, &ncol);
    /* init a header if it doesn't exist */
    if (rows==NULL) {
        rows = (char***)realloc(rows, (nrow+1)*sizeof(char**));
        rows[nrow++] = strparce(strdup(
                    "car model;"
                    "registration number;"
                    "owner's last name;"
                    "owner's initials;"
                    "quarterly mileage (array of four elements)"), ";", &ncol);
    }
    for (is_continue=1; is_continue; ) {
        printf("Enter:\n"
                "1: to display rows,\n"
                "2: to add a 1 row,\n"
                "3: to search by model,\n"
                "4: to search by mileage,\n"
                "anything else: to record and exit\n");
        fgets(buffer, sizeof(buffer), stdin);
        switch (feof(stdin)
                ? EXIT
                : atoi(buffer))
        {
        case DISPLAY:
            col_len = get_col_len(rows, nrow, ncol);
            if (nrow>1)
                printrows(rows, col_len, nrow, ncol, 1);
            else
                printf("\nempty\n\n");
            break;
        case ADD:
            fgets(buffer, sizeof(buffer), stdin);
            while (!is_valid(strdup(buffer), ";") && !feof(stdin)) {
                printf("try again\n");
                fgets(buffer, sizeof(buffer), stdin);
            }
            if (!feof(stdin)) {
                rows = (char***)realloc(rows, (nrow+1)*sizeof(char**));
                rows[nrow++] = strparce(buffer, ";", &ncol);
            }
            break;
        case SEARCH1:
            snrow = nrow;
            fgets(buffer, sizeof(buffer), stdin);
            srows = search_in_rows(rows, strndup(buffer, rtrimlen(buffer)), &snrow, match_by_num);
            if (srows!=NULL) {
                col_len = get_col_len(rows, nrow, ncol);
                printrows(rows, col_len, 1, ncol, 1);
                printrows(srows, col_len, snrow, ncol, 0);
            } else
                printf("not found\n");
            break;
        case SEARCH2:
            snrow = nrow;
            fgets(buffer, sizeof(buffer), stdin);
            srows = search_in_rows(rows, strndup(buffer, rtrimlen(buffer)), &snrow, match_by_mileage);
            if (srows!=NULL) {
                col_len = get_col_len(rows, nrow, ncol);
                printrows(rows, col_len, 1, ncol, 1);
                printrows(srows, col_len, snrow, ncol, 0);
            } else
                printf("not found\n");
            break;
        default:
            printf("\nsave\n");
            writerows(file, rows, nrow, ncol);
            is_continue = 0;
            break;
        }
    }

    fclose(file);
    return 0;
}

void
writerows(FILE *file, char ***rows, int nrow, int ncol) {
    int i, j;
    if (rows==NULL)
        return;
    rewind(file);
    ftruncate(fileno(file), 0);
    for (i=0; i<nrow; ++i)
        for (j=0; j<ncol; ++j)
            fprintf(file, (j<ncol-1)?"%s"DELIM:"%s\n", rows[i][j]);
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

long
rtrimlen(const char *s) {
    long len;
    for (len=(long)strlen(s)-1; len>=0 && isspace(s[len]); --len)
        ;
    return len+1;
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
    return strlen(smsg)>0 && strstr(row[0], smsg) == row[0];
}

int
match_by_mileage(char **row, const char *smsg) {
    int i, summ, snum;
    char *endptr;
    strtok(strdup(row[4]), " \t\n");
    for (i=1, summ=0; i<4; ++i)
        if (i==1 || i==2)
            summ+=atoi(strtok(NULL, " \t\n"));
        else
            strtok(NULL, " \t\n");
    snum = strtol(smsg, &endptr, 10);
    if (endptr!=smsg && (isspace(*endptr) || *endptr=='\0'))
        return summ<=snum;
    return 0;
}

int
is_valid(const char *line, const char *delim) {
    int i;
    char *token, *col2;
    for (i=0, col2=NULL, token=strtok(strdup(line), delim);
            token!=NULL;
            ++i, token=strtok(NULL, delim))
        if (i>=5) {
            return 0;
        }
        else if (i==4)
            col2=strdup(token);
    return col2==NULL?0:is_valid_4num(col2);
}

int
is_valid_4num(const char *line) {
    int i;
    char *token, *endptr;
    for (i=0, token=strtok(strdup(line), " \t\n");
            token!=NULL;
            ++i, token=strtok(NULL, " \t\n"))
    {
        strtol(token, &endptr, 10);
        if (!(i<4 && endptr!=token &&
             (*endptr==' ' ||
              *endptr=='\t' ||
              *endptr=='\n' ||
              *endptr=='\0')))
            return 0;
    }
    return 1;
}
