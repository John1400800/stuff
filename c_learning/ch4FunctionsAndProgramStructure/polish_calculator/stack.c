#include <stdio.h>

#define STACKSIZE 100

static int stack[STACKSIZE];
static unsigned curr_pos = 0;

int push(int n) {
    if (curr_pos < STACKSIZE) {
        stack[curr_pos++] = n;
    } else {
        printf("stack overflow\n");
    }
    return n;
}

int pop(void) {
    if (curr_pos > 0) {
        return stack[--curr_pos];
    }
    printf("stack is empty\n");
    return 0;
}
