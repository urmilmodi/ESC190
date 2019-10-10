#include<stdio.h>
#include<stdlib.h>

int lt(int x, int y);
int gt(int x, int y);
int bs(int *x, int size, int (*compare)(int x, int y));

int lt(int x, int y) {
    return x > y;
}

int gt(int x, int y) {
    return x < y;
}

int bs(int *x, int size, int (*compare)(int x, int y)) {
    int i = 0, j = 0;
    for (j = 0; j < size; j++) {

        for (i = 0; i < size - 1; i++) {
            if (compare(x[i], x[i + 1])) {
                int z = x[i];
                x[i] = x[i + 1];
                x[i + 1] = z;
            }
        }
    }
    return 0;
}