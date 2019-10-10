/* This is an example of how to use a linked list as a
 * dynamic container to store data that is input with an
 * unknown number of items.
 *
 * Note how we get the data:
 * -while loop (because the number of iterations is unknown)
 * -scanf returns EOF, or End-Of-File, when "nothing" has been input
 * -for each iteration, we stuff the input data into a linked list
 *
 * Usage:
 * gcc getData.c
 * echo "1 2 3 4 5 6 7 8     9      10" | ./a.out
 * should report 10 items read and dump it out
 * -> white space is ignored (space, tab, return)
 *
 * Assignment:
 * -modify this code so that it handles input "char" data
 *  rather than ints (trivial modification)
 * echo "abcdef" | ./a.out
 * should report 7 items read
 * (white space is representable by the char hence the
 * final return you enter is stored as a char)
 */

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
   int n=0;
   char popped;
   char value;
   int rvalue=0;
   int i = 0;
   llnode *input_list=NULL;
   while (scanf("%c",&value) != EOF) {
      n++;
      push(&input_list,value);
   }
   printf("INFO: you entered %d items\n",n);
   rvalue=llnode_print_from_tail(input_list);
   for (i = 0; i < n; i++) {
      rvalue= pop(&input_list, &popped);
      printf("pop return: %d\n", rvalue);
      printf("popped: %c\n", popped);
      rvalue=llnode_print_from_tail(input_list);
      printf("print return: %d\n", rvalue); 
   };
   if (!(rvalue==0)) {printf("ERR: llnode_print returned an error\n");}
   return 0;
}
