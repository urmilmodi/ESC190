#include<stdio.h>
#include<stdlib.h>

typedef struct {
   int *store;
   unsigned int size;
   unsigned int end;
} HeapType;

int initHeap(HeapType *pHeap, int size);
int inorder(HeapType *pHeap, int **output, int *o_size);
int inordered(HeapType *pHeap, int **output, int *o_size, int i);
int preorder(HeapType *pHeap, int **output, int *o_size);
int preordered(HeapType *pHeap, int **output, int *o_size, int i);
int postorder(HeapType *pHeap, int **output, int *o_size);
int postordered(HeapType *pHeap, int **output, int *o_size, int i);
int addHeap(HeapType *pHeap, int key);
int findHeap(HeapType *pHeap, int key);
int delHeap(HeapType *pHeap, int *key);
int resize(HeapType *pHeap);
int fixup(HeapType *pHeap);
int fixdown(HeapType *pHeap);
int parentindex(int n);

int initHeap(HeapType *pHeap, int size) {
    if (pHeap == NULL || size < 1) {return -1;}
    (pHeap->store) = (int *)malloc(sizeof(int)*size);
    if (pHeap->store == NULL) {return -1;}
    pHeap->end = 0;
    pHeap->size = size;
    return 0;
}

int addHeap(HeapType *pHeap, int key) {
    if (pHeap == NULL) {return -1;}
    resize(pHeap);
    pHeap->store[pHeap->end] = key;
    (pHeap->end)++; 
    resize(pHeap);
    fixup(pHeap);
    return 0;
}

int resize(HeapType *pHeap) {
    int *new = NULL;
    int i = 0;
    if (pHeap == NULL) {return -1;}
    if (pHeap->end == pHeap->size) {
        new = malloc(sizeof(int)*2*(pHeap->size));
        if (new == NULL) {return -1;}
        for (i = 0; i < pHeap->size; i++) {
            new[i] = pHeap->store[i];
        }
        pHeap->size = 2*(pHeap->size);
        pHeap->store = new;
    }
    return 0;
}

int findHeap(HeapType *pHeap, int key) {
    int i = 0;    
    if (pHeap == NULL) {return -1;}
    for (i = 0; i < pHeap->end; i++) {
        if (pHeap->store[i] == key) {
            return 1;
        }
    }
    return 0;
}

int delHeap(HeapType *pHeap, int *key) {
    if (pHeap == NULL || pHeap->end == 0) {return -1;}
    *key = pHeap->store[0];
    pHeap->store[0] = pHeap->store[pHeap->end - 1];
    pHeap->end = pHeap->end - 1;
    fixdown(pHeap);
    return 0;
}

int fixup(HeapType *pHeap) {
    int i = 0, j = 0, k = 0;
    if (pHeap == NULL) {return -1;}
    for (j = pHeap->end; j > 0; j--) {
        for (i = j; i > 0; i--) {
            k = i;
            while (i != 0) {
                if (pHeap->store[i - 1] > pHeap->store[parentindex(i - 1)]) {
                    pHeap->store[parentindex(i - 1)] += pHeap->store[i - 1];
                    pHeap->store[i - 1] = pHeap->store[parentindex(i - 1)] - pHeap->store[i - 1];
                    pHeap->store[parentindex(i - 1)] -= pHeap->store[i - 1];
                    i = parentindex(i - 1);
                } else {break;}
            }
            i = k;
        }
    }
    return 0;
}

int fixdown(HeapType *pHeap) {
    int i = 0, j = 0, k = 0;
    if (pHeap == NULL) {return -1;}
    for (j = 0; j < pHeap->end; j++) {
        for (i = j; i < pHeap->end; i++) {
            k = i;
            while (i != pHeap->end) {
                if (2*i + 1 < pHeap->end && pHeap->store[i] < pHeap->store[2*i + 1]) {
                    pHeap->store[2*i + 1] += pHeap->store[i];
                    pHeap->store[i] = pHeap->store[2*i + 1] - pHeap->store[i];
                    pHeap->store[2*i + 1] -= pHeap->store[i];
                    i = 2*i + 1;

                } else if (2*i + 2 < pHeap->end && pHeap->store[i] < pHeap->store[2*i + 2]) {
                    pHeap->store[2*i + 2] += pHeap->store[i];
                    pHeap->store[i] = pHeap->store[2*i + 2] - pHeap->store[i];
                    pHeap->store[2*i + 2] -= pHeap->store[i];
                    i = 2*i + 2;

                } else {break;}
            }
            i = k;
        }
    }
    return 0;
}

int parentindex(int n) {
    return (n/2) - (n/2)%1;
}

int inorder(HeapType *pHeap, int **output, int *o_size) {
    if (pHeap == NULL || output == NULL || o_size == NULL) {return -1;}
    (*output) = (int *)malloc(sizeof(int)*(pHeap->end));
    if ((*output) == NULL) {return -1;}
    inordered(pHeap, output, o_size, 0);
    *o_size = pHeap->end;
    return 0;
}

int inordered(HeapType *pHeap, int **output, int *o_size, int i) {
    if (pHeap == NULL || output == NULL || o_size == NULL) {return -1;}
    if (i < pHeap->end) {
        inordered(pHeap, output, o_size, 2*i + 1);
        (*output)[*o_size] = (pHeap->store)[i];
        (*o_size)++;
        inordered(pHeap, output, o_size, 2*i + 2);
    }
    return 0;
}

int preorder(HeapType *pHeap, int **output, int *o_size) {
    if (pHeap == NULL || output == NULL || o_size == NULL) {return -1;}
    (*output) = (int *)malloc(sizeof(int)*(pHeap->end));
    if ((*output) == NULL) {return -1;}
    *o_size = 0;
    preordered(pHeap, output, o_size, 0);
    *o_size = pHeap->end;
    return 0;
}

int preordered(HeapType *pHeap, int **output, int *o_size, int i) {
    if (pHeap == NULL || output == NULL || o_size == NULL || i < 0) {return -1;}
    if (i < pHeap->end) {
        (*output)[*o_size] = (pHeap->store)[i];
        if (2*i + 1 < pHeap->end) {
            (*o_size)++;
            preordered(pHeap, output, o_size, 2*i + 1);
        }
        if (2*i + 2 < pHeap->end) {
            (*o_size)++;
            preordered(pHeap, output, o_size, 2*i + 2);
        }
    } else {
        return 1;
    }
    return 0;
}

int postorder(HeapType *pHeap, int **output, int *o_size) {
    if (pHeap == NULL || output == NULL || o_size == NULL) {return -1;}
    (*output) = (int *)malloc(sizeof(int)*(pHeap->end));
    if ((*output) == NULL) {return -1;}
    *o_size = 0;
    postordered(pHeap, output, o_size, 0);
    *o_size = pHeap->end;
    return 0;
}

int postordered(HeapType *pHeap, int **output, int *o_size, int i) {
    if (pHeap == NULL || output == NULL || o_size == NULL || i < 0) {return -1;}
    if (i < pHeap->end) {
        if (2*i + 1 < pHeap->end) {
            postordered(pHeap, output, o_size, 2*i + 1);
        }
        if (2*i + 2 < pHeap->end) {
            postordered(pHeap, output, o_size, 2*i + 2);
        }
        (*output)[*o_size] = (pHeap->store)[i];
        (*o_size)++;
    } else {
        return 1;
    }
    return 0;
}
