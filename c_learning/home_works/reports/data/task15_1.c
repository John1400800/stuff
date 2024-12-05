#include <stdio.h>

int main(void) {
    FILE *file;
    int x, y, n, k;
    char op1, op2;

    file = fopen("input.txt", "r+");
    fscanf(file, "У меня спросили: сколько будет %d %c %d ?\n", &x, &op1, &y);
    fscanf(file, "А я не знаю! А %d %c %d Тоже!", &n, &op2, &k);
    fprintf(file, "%d %c %d = %d\n"
           "%d %c %d = %d\n",
           x, op1, y, op1=='+'?x+y:op1=='-'?x-y:op1=='*'?x*y:op1=='/'?x/y:0,
           n, op2, k, op2=='+'?k+n:op2=='-'?k-n:op2=='*'?k*n:op2=='/'?k/n:0);
    fclose(file);
    return 0;
}
