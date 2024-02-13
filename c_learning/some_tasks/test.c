#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#ifndef NULL
#define NULL ((void *)0)
#endif

#ifndef _INC_STDLIB
//// note: stupid implementation and even dumber without limits.h :)
#define NEXT_TYPE long long
#define RAND_TYPE short /*RAND_TYPE <= NEXT_TYPE for more "random" results */

#define NEXT_SIZE sizeof(NEXT_TYPE)
#define RAND_MAX_SIZE sizeof(RAND_TYPE)
#define RAND_MAX ((1ull<<(RAND_MAX_SIZE)*8)-1)
#define HALF_SHIFT ((NEXT_SIZE*8-RAND_MAX_SIZE*8)/2) /*narrowing the range of "NEXT" to "RANDOM"*/

void srand(unsigned RAND_TYPE seed);
#define srand(init) srand((unsigned RAND_TYPE)(init))
unsigned RAND_TYPE rand(void);
#endif

#define rrand(low, high) ((low)+rand()%((high)-(low)+1)) 


int main(void) {
    int i;
    srand(time(NULL));
    for (i = 0; i < 500; ++i)
        printf("%10d, ", rrand(-5, 5));

    RAND_MAX;
    return 0;
}

#ifndef _INC_STDLIB
static unsigned NEXT_TYPE next = 1;

unsigned RAND_TYPE rand(void) {
    next = next * 1103515245 + 12345;
    return (unsigned RAND_TYPE)(next<<HALF_SHIFT>>HALF_SHIFT>>HALF_SHIFT)%(RAND_MAX+1);
}

void srand(unsigned RAND_TYPE seed) {
    next = seed;
} 
#endif
