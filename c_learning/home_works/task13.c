#include <stdlib.h>
#include <ctype.h>
#include <stdbool.h>
#include <string.h>
#include <stdio.h>

#ifndef _CTYPE_H
#define isspace(c) ((c) == ' ' || (unsigned)(c)-'\t' < 5)
#endif // _CTYPE_H

#define BUFFSIZE 1024

char *rev_words_in_sentence(const char *src);

int main(void) {
    char inpbuff[BUFFSIZE];
    printf("%s\n", rev_words_in_sentence(fgets(inpbuff, BUFFSIZE, stdin)));
    return EXIT_SUCCESS;
}

char *rev_words_in_sentence(const char *src) {
    char *res = malloc(strlen(src)+1);
    strcpy(res, src);
    char *start_word_ptr, *end_word_ptr;
    for (start_word_ptr = end_word_ptr = res;
            *start_word_ptr != '\0';
            ++end_word_ptr)
    {
        if (isspace(*start_word_ptr)) {
            ++start_word_ptr;
            continue;
        }
        if (isspace(end_word_ptr[1]) || end_word_ptr[1] == '\0')
        {
            char *temp_ptr;
            for (temp_ptr = end_word_ptr+1;
                    start_word_ptr < end_word_ptr;
                    --end_word_ptr, ++start_word_ptr)
            {
                char temp = *start_word_ptr;
                *start_word_ptr = *end_word_ptr;
                *end_word_ptr   = temp;
            }
            start_word_ptr = end_word_ptr = temp_ptr;
        }
    }
    return res;
}
