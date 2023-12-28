#include <stdio.h>
#include <stdlib.h>
#include "common.h"

int main(void) {
    int op1;
    char buff[100];
    char type;
    char f = 1;
    while (f) {
        type = get_next(buff);
        switch (type) {
        case NUM:
            push(atoi(buff));
            break;
        case OP:
            switch (buff[0]) {
            case '+':
                push(pop() + pop());
                break;
            case '-':
                op1 = pop();
                push(pop() - op1);
                break;
            case '*':
                push(pop() * pop());
                break;           
            }
            break;
        default:
            printf("%d", pop());
            f = 0;
            break;
        }
    }
}
