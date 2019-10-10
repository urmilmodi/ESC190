#include <stdio.h>

void bin (unsigned n);
int main(void) {
    unsigned int x = 0xffffffff;
    bin(x);
    bin((x>>22)&(0x7));
    bin((x<<16)>>16);
    return 0;
}

void bin(unsigned n) 
{ 
    unsigned i; 
    for (i = 1 << 31; i > 0; i = i / 2) 
        (n & i)? printf("1"): printf("0"); 
    printf("\n");
} 