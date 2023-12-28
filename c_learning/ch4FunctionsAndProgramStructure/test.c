#ifndef _INC_STDIO 
    #include <stdio.h>
#endif

#define max(a, b) ((a) > (b) ? (a) : (b))
#define square(x) ((x) * (x))
#define dstr(arg) #arg
#define concat(arg1, arg2) arg1 ## arg2
#define swap(type, x, y)                                                       \
    type temp = (x);                                                           \
    x = (y);                                                                   \
    (y) = temp

#undef OOPS

int main(void) {
    printf(dstr(concat(hello, world)) "");
    printf(dstr(2+1) "%d", square(2+1));
}
