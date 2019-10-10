#include<stdio.h>
#include<stdlib.h>

unsigned char prng(unsigned char x, unsigned char pattern);
unsigned char FSR(unsigned char x);
unsigned char FSL(unsigned char x);
int crypt(char *data, unsigned int size, unsigned char password);

unsigned char prng(unsigned char x, unsigned char pattern) {
    
    return (unsigned char) FSL(x) ^ pattern;
}

unsigned char FSR(unsigned char x) {

    return (unsigned char) ((x >> 1) | (x & 0x1) << 7);
}

unsigned char FSL(unsigned char x) {

    return (unsigned char) ((x << 1) | (x & (0x1<<7)) >> 7);
}


void bin(unsigned n) 
{ 
    unsigned i; 
    for (i = 1 << 31; i > 0; i = i / 2) 
        (n & i)? printf("1"): printf("0"); 
    printf("\n");
} 

int crypt(char *data, unsigned int size, unsigned char password) {
    if (password < 0 || size < 0) {
        return -1;
    }
    int prngVal = password;
    for (int i = 0; i < size; i++) {
       prngVal = prng(prngVal, 0xb8);
       data[i] = (data[i]) ^ prngVal;
    }
    return 0;
}

int main(void) {
    unsigned char x = 0xef;
    bin(x);
    x = FSL(x);
    bin(x);
    x = FSL(x);
    bin(x);
    x = FSL(x);
    bin(x);
    x = FSL(x);
    bin(x);
    x = FSL(x);
    bin(x);
    x = FSL(x);
    bin(x);
    x = FSL(x);
    bin(x);
    x = FSL(x);
    bin(x);
    x = FSL(x);
    bin(x);
    char y[] = "....";
    unsigned char password = 0x7;
    printf("%s\n", x);
    crypt(x, (unsigned int) sizeof(x)/sizeof(char), password);
    printf("%s\n", x);
    crypt(x, (unsigned int) sizeof(x)/sizeof(char), password);
    printf("%s\n", x);
    return 0;
}