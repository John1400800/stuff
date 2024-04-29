#include <stdio.h>

#define isspace(c) (((c) >= 9 && (c) <= 13) || (c) == 32)

typedef enum { OUT, IN } State;

void wrap_str(char *start_linep, int lim);

int main(void) {
    char s[] = "* **** ******* ********** ************** ** *********** "
               "**** ****** ******************* ********* ********* * "
               "*********** * *** ****** ******** *** ********* "
               "********* ********** ** *** ******** *** * ***** ******* "
               "*************** *** ********* ************ ***** *** "
               "***** ********** ********* ******** ********* ****** *** "
               "**** ********* **** ******* * ******** * ** * **** ****** "
               "******* *********** *** **** ** ********* **** **********";
    wrap_str(s, 16);
    printf("%s", s);
    return 0;
}

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
