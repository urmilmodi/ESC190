#include<stdio.h>
#include<stdlib.h>
#include "heap.c"

int main(void) {
    int i = 0, key = 156, o_size = 0;
    int *new = NULL;
    HeapType *pHeap = malloc(sizeof(HeapType));
    pHeap->store = malloc(sizeof(int)*25);
    pHeap->end = 10;
    pHeap->size = 25;
    i = 0;
    for (i = 0; i < 10; i++) {
        (pHeap->store)[i] = 10 - i;
    }
    printf("Manual Input\n");
    for (i = 0; i < pHeap->end; i++) {
        printf("%d\n", (pHeap->store)[i]);
    }
    key = 156;
    printf("Delete Test\n");
    printf("Before: %d\n", key);
    delHeap(pHeap, &key);
    printf("After: %d\n", key);

    printf("Remaining\n");
    for (i = 0; i < pHeap->end; i++) {
        printf("%d\n", (pHeap->store)[i]);
    }

    printf("Find 9 in Heap: %d\n", findHeap(pHeap, 9));
    printf("Find 0 in Heap: %d\n", findHeap(pHeap, 0));

    new = NULL;
    o_size = 0;
    inorder(pHeap, &new, &o_size);
    printf("Inorder: \n");
    for (i = 0; i < o_size; i++) {
        printf("%d ", new[i]);
    }

    new = NULL;
    o_size = 0;
    preorder(pHeap, &new, &o_size);
    printf("\nPreorder: \n");
    for (i = 0; i < o_size; i++) {
        printf("%d ", new[i]);
    }

    new = NULL;
    o_size = 0;
    postorder(pHeap, &new, &o_size);
    printf("\nPostorder: \n");
    for (i = 0; i < o_size; i++) {
        printf("%d ", new[i]);
    }
    pHeap = NULL;
    pHeap = malloc(sizeof(HeapType));
    printf("\nNew Heap\n");
    initHeap(pHeap, 25);
    for (i = 0; i < 10; i++) {
        addHeap(pHeap, i);
    }
    for (i = 0; i < pHeap->end; i++) {
        printf("%d\n", (pHeap->store)[i]);
    }
    return 0;
}