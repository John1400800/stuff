#include <stdio.h>
#include <stdlib.h>

#define UNKN 0
#define NUM  1
#define OP   2

int push(int n);
int pop(void);
char get_next(char *buff);

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


static char is_digit(char c) {
    if (c >= '0' && c <= '9') {
        return NUM;
    }
    return UNKN;
}

static char is_operator(char c) {
    if (c == '+' || c == '-' || c == '*' || c == '/') {
        return OP;
    }
    return UNKN;
}

char get_next(char *buff) {
    static char prevch = ' ';
    unsigned i = 0;
    char type = UNKN;

    while (1)
    {
        if (prevch == ' ') {
            prevch = getchar();
            if (i == 0) {
                continue;
            }
        }
        buff[i] = prevch;
        if (is_digit(prevch) && (type == UNKN || type == NUM)) {
            type = NUM;
        } else if (is_operator(prevch) && type == UNKN) {
            type = OP;
        } else {
            break;
        }
        ++i;
        prevch = ' ';
    }
    if (type == UNKN) {
        ++i;
    }
    buff[i] = '\0';
    return type;
}
