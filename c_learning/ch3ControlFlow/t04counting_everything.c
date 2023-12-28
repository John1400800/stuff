#include <stdio.h>

int main() {
    unsigned i, nwhite, nother, ndigit[10];
    char curr_ch, prev_ch = '\n';
    nother = nwhite = 0;
    for (i = 0; i < 10; ++i) {
        ndigit[i] = 0;
    }
    
    while (((curr_ch = (char)getchar()) != '\n' || prev_ch != '\n') && curr_ch != EOF) {
        switch (curr_ch) {
        case '0' : case '1' : case '2' : case '3' : case '4' :
        case '5' : case '6' : case '7' : case '8' : case '9' :
            ++ndigit[curr_ch - '0'];            
            break;
        case ' ' : case '\t' : case '\n' :
            ++nwhite;
            break;
        default :
            ++nother;
            break;
        }        
        prev_ch = curr_ch;
    } 
    printf ("nums =");
    for (i = 0; i < 10; i++)
        printf (" %d", ndigit[i]);
    printf(", white = %d, other = %d\n",
            nwhite, nother);
    return 0;
}    
