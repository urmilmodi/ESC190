#include<stdio.h>
#include<stdlib.h>

struct bstNode {
    int val;
    struct bstNode *l;
    struct bstNode *r;
};
typedef struct bstNode bstNode;

int add_bst(bstNode **root,int val);
int printTreeInOrder(bstNode *root);
int printLevelOrder(bstNode *root);
int GivenLevel(bstNode *root, int level);
int height(bstNode *root);

int add_bst(bstNode **root,int val) {
    if (root == NULL) {return -1;}
    if (*root == NULL) {
        (*root) = malloc(sizeof(bstNode));
        if (*root == NULL) {return -1;}
        (*root)->val = val;
        (*root)->l = NULL;
        (*root)->r = NULL;
        return 0;
    } else {
        if (val < (*root)->val) {
            return add_bst(&((*root)->l), val);

        } else if (val > (*root)->val) {
            return add_bst(&((*root)->r), val);
        }
    }
}

int printTreeInOrder(bstNode *root) {
    if (root == NULL) {return -1;}
    if (root->l != NULL) {
        printTreeInOrder(root->l);
    }
    printf("%d\n", root->val);
    if (root->r != NULL) {
        printTreeInOrder(root->r);
    }
    return 0;
}

int printLevelOrder(bstNode *root) {
    if (root == NULL) {return -1;}
    int h = height(root);
    int i = 0;
    for (i = 1; i < h + 1; i++) {
        GivenLevel(root, i);
    }
    return 0;
}

int GivenLevel(bstNode *root, int level) {
    if (root == NULL) {return -1;}
    if (level == 1) {
        printf("%d ", root->val);

    } else if (level > 1) {
        if (root->l != NULL) {
            GivenLevel(root->l, level - 1);
        }
        if (root->r != NULL) {
            GivenLevel(root->r, level - 1);
        }
    }
    return 0;
}

int height(bstNode *root) {
    if (root == NULL) {return -1;}
    int lheight = 0;
    int rheight = 0;
    if (root->l != NULL) {
        lheight = height(root->l);
    }
    if (root->r != NULL) {
        rheight = height(root->r);
    }
    if (lheight > rheight) {
        return lheight + 1;
    } else {
        return rheight + 1;
    }
}

int main(void) {
    bstNode *root=NULL;
    int n = 0;
    int value = 0;
    int rvalue = 0;

    while (scanf("%d",&value) != EOF) {
       add_bst(&root, value);
    }

    printTreeInOrder(root);
    return 0;
}