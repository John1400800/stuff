#include <stdio.h>

#define STACKSIZE 3

static int stack[STACKSIZE];
static int *stackp = stack;

// 0123
void push(int n) {
    if (stackp - stack < STACKSIZE) 
        *stackp++ = n;
    else
        printf("push: stack overflow\n");
}

int pop(void) {
    if (stackp - stack > 0)
        return *--stackp;
    printf("pop: stack empty\n");
    return 0;
}

int main(void) {
    pop();
    push(1);
    push(2);
    push(3);
    push(4);
    printf("%d\n", pop());
    push(4);
    printf("%d\n", pop());
    printf("%d\n", pop());
    printf("%d\n", pop());
    pop();
}
