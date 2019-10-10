#include<stdio.h>
#include<stdlib.h>

typedef struct intlist {

   int *x;
   int end;
   int len;
} intlist;

int init(intlist *l,int len) {

   if (l==NULL) { return -1; }

   (l->x) = (int *)malloc(len * sizeof(int));
   if ((l->x) == NULL) { return -1; }

   l->len = len;
   l->end = -1;

   return 0;
}

int add_to_end(intlist *l,int val) {
    if (l == NULL) {return -1;}
    if ((l->x) == NULL) { return -1; }
    if (l->end == l->len - 1) {

        if (extend(l) == -1) {return -1;}
    }
    (l->x)[l->end + 1] = val;
    l->end = l->end + 1;
    return 0;
}
int add_to_start(intlist *l,int val) {
    if (l == NULL) {return -1;}
    if ((l->x) == NULL) { return -1; }
    if (l->end == l->len - 1) {

        if (extend(l) == -1) {return -1;}
        return add_to_start(l, val);
    }
    int i = 0;
    for (i = l->end; i > 1; i--) {
        (l->x)[i] = (l->x)[i - 1];
    }
    (l->x)[0] = val;
    l->end = l->end + 1;
    return 0;
}

int findvalue(intlist *l, int value, int *location) {
    if (l == NULL) {return -1;}
    if ((l->x) == NULL) { return -1; }
    int i = 0;
    int test = 0;
    for (i = 0; i < l->end + 1; i++) {
        if ((l->x)[i] == value) {
            test = 1;
            if (*location != NULL) {*location = i;}
            break;
        }
    }
    if (test == 0) {return -1;}
    return 0;
}

int insertval(intlist *l, int value, int location) {
    if (l == NULL) {return -1;}
    if ((l->x) == NULL) { return -1; }
    if (l->end == location) {return add_to_end(l, value);}
    int i = 0;
    for (i = l->end; i > location + 1; i--) {
        (l->x)[i] = (l->x)[i - 1];
    }
    (l->x)[location] = value;
    l->end = l->end + 1;
    return 0;    
}

int insertafter(intlist *l,int insert_val,int val) {
    if (l == NULL) {return -1;}
    if ((l->x) == NULL) { return -1; }
    int i = 0;
    int location;
    if (findvalue(l, val, &location) == -1) {return -1;}
    if (l->end == location) {return add_to_end(l, insert_val);}
    return (insertval(l, insert_val, location));
}

int deletevalue(intlist *l, int value) {
    if (l == NULL) {return -1;}
    if ((l->x) == NULL) { return -1; }
    int i = 0;
    int location;
    if (findvalue(l, value, &location) == -1) {return -1;}

    for (i = location; i < l->end + 1; i++) {
        (l->x)[i] = (l->x)[i + 1];
    }
    return 0;
}

int extend(intlist *l) {
    if (l == NULL) {return -1;}
    if ((l->x) == NULL) { return -1; }
    int i = 0;
    int *x = NULL;
    x = (int *)malloc(2*(l->len)*sizeof(int));
    if (x == NULL) {return -1;}

    for (i = 0; i < l->len; i++) {
        x[i] = (l->x)[i];
    }
    free(l->x);
    l->x = x;
    l->len = 2*(l->len);
    return 0;
}

int push(intlist *l, int value) {
    if (l == NULL) {return -1;}
    if ((l->x) == NULL) { return -1; }
    return add_to_end(l, value);
}

int pop(intlist *l, int *rv) {
    if (l == NULL) {return -1;}
    if ((l->x) == NULL) { return -1; }
    *rv = (l->x)[l->end];
    return deletevalue(l, *rv);
}

int enqueue(intlist *l, int value) {
    if (l == NULL) {return -1;}
    if ((l->x) == NULL) { return -1; }
    return add_to_end(l, value);
}

int dequeue(intlist *l, int *rv) {
    if (l == NULL) {return -1;}
    if ((l->x) == NULL) { return -1; }
    *rv = (l->x)[0];
    return deletevalue(l, *rv);
}

int main(int argc, char const *argv[])
{
    /* code */
    return 0;
}
