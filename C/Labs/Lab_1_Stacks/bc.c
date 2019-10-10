#include <stdio.h>
#include <stdlib.h>

struct llnode {
   char value;
   struct llnode *next;
};
typedef struct llnode llnode;

int llnode_add_to_head(llnode **x, char value) {

   if (x == NULL) {
      return -1;
   } else {

      llnode *y = *x;
      (*x) = (llnode *)malloc(sizeof(llnode));
      (*x)->value = value;
      (*x)->next = y;
      return 0;
   }
}

int llnode_add_to_tail(llnode **x,char value) {
   if (x==NULL) { return -1; }
   if (*x==NULL) {
      *x = (llnode *) malloc(sizeof(llnode));
      (*x)->value = value;
      (*x)->next = NULL;
      return 0;
   } else {
      return llnode_add_to_tail(&((*x)->next),value);
   }
}

int llnode_print_from_head(llnode *x) {
   if (x==NULL) { return 0; }
   else {
      printf("%c\n",x->value);
      return llnode_print_from_head(x->next);
   }
}

int llnode_print_from_tail(llnode *x) {
   if (x==NULL) { return 0; }
   else {
      if (x->next == NULL) {
         printf("%c\n",x->value);
	      return 0;
      } else {
         llnode_print_from_tail(x->next);
         printf("%c\n",x->value);
	 return 0;
      }
   }
}

int push(llnode **x, char value) {
   if (x == NULL) {return -1;}
   int rvalue = 0;
   rvalue = llnode_add_to_tail(x, value);
   return rvalue;
}

int pop(llnode **x, char *return_value) {
   llnode *y = *x;
   if (x == NULL) {return -1;}
   if (*x == NULL) {return -1;}
   if (y->next == NULL) {
      *return_value = y->value;
      free(y);
      y = NULL;
      return 0;
   }
   while (y->next->next != NULL) {
      y = y->next;
   }
   *return_value = y->next->value;
   free(y->next);
   y->next = NULL;
   return 0;
}

int main(void) {
    char pvalue = 0;
    char value = 0;
    int r = 0;
    int i = 0;
    llnode *A = NULL;
    while (scanf("%c",&value) != EOF) {
        if (value == '{') {
            push(&A, value);
            //llnode_print_from_head(A);

        } else if (value == '}') {
            r = pop(&A, &pvalue);
            printf("} Popped Value: %c\n", pvalue);
            
            if(pvalue != '{') {
               printf("FAIL,%d\n", i);
               return -1;
            }
        
        } else if (value == '(') {
            push(&A, value);
            //llnode_print_from_head(A);

        } else if (value == ')') {
            r = pop(&A, &pvalue);
            printf(") Popped Value: %c\n", pvalue);
            
            if(pvalue != '(') {
               printf("FAIL,%d\n", i);
               return -1;
            }

        } else if (value == '[') {
            push(&A, value);
            //llnode_print_from_head(A);

        } else if (value == ']') {
            r = pop(&A, &pvalue);
            printf("] Popped Value: %c\n", pvalue);

            if(pvalue != '[') {
               printf("FAIL,%d", i);
               return -1;
            }
        }
        i++;
    }

    if (pop(&A, &pvalue) == 0) {
        printf("FAIL,%d", i);
        return -1;
    }
    printf("PASS");
    return 0;
}