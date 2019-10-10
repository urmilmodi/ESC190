#include <stdio.h>
#include <stdlib.h>

int sq(int x) {
   return x*x;
}

int cu(int x) {
   return x*x*x;
}

int driver(int (*f)(int), int x) {
   return (*f)(x);
}

int main(void) {
   int j = 0;
   int (*g)(int) = cu;
   printf("adx of function sq: %p\n", sq);
   printf("adx of function cu: %p\n", cu);
   for (j = 0;j < 0xa;j++){
      printf("%d: %d %d\n", j, driver(cu,j), (*g)(j));
   }
}