#include<stdio.h>
#include<stdlib.h>

typedef struct {
   int *store;
   unsigned int size;
   unsigned int end;
   int (*compare)(int x,int y);
} intHeap_T;

int lt(int x, int y);
int gt(int x, int y);
int store(intHeap_T* heap, int value);
int retrieve(intHeap_T* heap, int *rvalue);

int lt(int x, int y) {
    return x < y;
}

int gt(int x, int y) {
    return x > y;
}

int store(intHeap_T* heap, int value) {
    if ((*heap).end == (*heap).size) {return -1;}
    (*heap).store[(*heap).end] = value;
    (*heap).end++;
    for (int i = (*heap).end - 1; i > -1; i--) {
        int j = i;
        while (1) {
            if ((*heap).compare((*heap).store[j/2 - (j/2)%1], (*heap).store[j])) {
                int temp = (*heap).store[j];
                (*heap).store[j] = (*heap).store[j/2 - (j/2)%1];
                (*heap).store[j/2 - (j/2)%1] = temp;
                j = j/2 - (j/2)%1;
            } else {break;}
        }
    }
    return 0;
}

int retrieve(intHeap_T* heap, int *rvalue) {
    if ((*heap).end == 0) {return -1;}
    *rvalue = (*heap).store[0];
    (*heap).store[0] = (*heap).store[(*heap).end - 1];
    (*heap).end = (*heap).end - 1;
    for (int k = 0; k < (*heap).end; k++) {
        for (int i = 0; i < (*heap).end; i++) {
            int j = i;
            while (1) {
                if (2*j + 1 < (*heap).end && (*heap).compare((*heap).store[j], (*heap).store[2*j + 1])) {
                    int temp = (*heap).store[j];
                    (*heap).store[j] = (*heap).store[2*j + 1];
                    (*heap).store[2*j + 1] = temp;
                    j = 2*j + 1;
                
                } else if (2*j + 2 < (*heap).end && (*heap).compare((*heap).store[j], (*heap).store[2*j + 2])) {
                    int temp = (*heap).store[j];
                    (*heap).store[j] = (*heap).store[2*j + 2];
                    (*heap).store[2*j + 2] = temp;
                    j = 2*j + 2;
                
                } else {break;}
            }
        }
    }
    return 0;
}