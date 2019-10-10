#include<stdio.h>
#include<stdlib.h>
#include "avlrot.c"

int main(void) {
    avlNode *root=NULL;
    addAvl(&root,7);
    addAvl(&root,5);
    addAvl(&root,3);
    addAvl(&root,1);
    addAvl(&root,4);
    addAvl(&root,6);
    addAvl(&root,8);
    printTreeInOrder(root);
    printLevelOrder(root);
    avlNode *roott=NULL;
    addAvl(&roott,5);
    addAvl(&roott,7);
    addAvl(&roott,3);
    addAvl(&roott,1);
    addAvl(&roott,4);
    addAvl(&roott,6);
    addAvl(&roott,8);
    printTreeInOrder(roott);
    printLevelOrder(roott);
    return 0;
}