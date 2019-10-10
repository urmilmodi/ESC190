#include<stdio.h>
#include<stdlib.h>

struct avlNode {
    int balance; /* -1 Left, 0 balanced, +1 Right */
    int val;
    struct avlNode *l;
    struct avlNode *r;
};
typedef struct avlNode avlNode;

struct qNode {
    avlNode *pval;
    struct qNode *nxt;
};

int isAVL(avlNode **root);
int printTreeInOrder(avlNode *root);
int printLevelOrder(avlNode *root);
int rotate(avlNode **root, unsigned int Left0_Right1);
int height(avlNode *root);
int dblrotate(avlNode **root, unsigned int MajLMinR0_MajRMinL1);
int fix(avlNode **root);
int GivenLevel(avlNode *root, int level);
int addAvl(avlNode **root, int val);

int printTreeInOrder(avlNode *root) {
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

int printLevelOrder(avlNode *root) {
    if (root == NULL) {return -1;}
    int h = height(root);
    int i = 0;
    for (i = 1; i < h + 1; i++) {
        GivenLevel(root, i);
    }
    return 0;
}

int GivenLevel(avlNode *root, int level) {
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

int isAVL(avlNode **root) {
    if (root == NULL) {return -1;}
    int lheight = 0;
    int rheight = 0;
    if ((*root)->l != NULL) {
        lheight = height((*root)->l);
    }
    if ((*root)->r != NULL) {
        rheight = height((*root)->r);
    }
    if (lheight - rheight == -1 || lheight - rheight == 1 || lheight - rheight == 0) {
        return 0;

    } else {
        return -1;
    }
}

int height(avlNode *root) {
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

int rotate(avlNode **root, unsigned int Left0_Right1) {
    if (root == NULL) {return -1;}
    if (*root == NULL) {return -1;}
    if (Left0_Right1 == 0) {
        // Rotate Left, put right node to main

        avlNode *x = (*root)->r;
        avlNode *y = x->l;
    
        x->l = (*root);
        (*root)->r = y;
        (*root) = x;
    } else if (Left0_Right1 == 1) {
        // Rotate Right, put left node to main
        
        avlNode *x = (*root)->l;
        avlNode *y = x->r;
    
        x->r = (*root);
        (*root)->l = y;
        (*root) = x;
    }
    return 0;
}

int dblrotate(avlNode **root, unsigned int MajLMinR0_MajRMinL1) {
    if (root == NULL) {return -1;}
    if (*root == NULL) {return -1;}
    if (MajLMinR0_MajRMinL1 == 0) {
        if (rotate(&((*root)->l), 0) == -1) {
            return -1;
        }
        rotate(root, 1);
        
    } else if (MajLMinR0_MajRMinL1 == 1) {
        if (rotate(&((*root)->r), 1) == -1) {
            return -1;
        }
        rotate(root, 0);
    }
    return 0;
}

int addAvl(avlNode **root, int val) {
    if (root == NULL) {return -1;}
    if (*root == NULL) {
        (*root) = malloc(sizeof(avlNode));
        if (*root == NULL) {return -1;}
        (*root)->val = val;
        (*root)->l = NULL;
        (*root)->r = NULL;
        return 0;
    } else {
        if (val < (*root)->val) {
            addAvl(&((*root)->l), val);
        } else if (val > (*root)->val) {
            addAvl(&((*root)->r), val);
        }
    }
    fix(root);
    // Check if this makes sure its proper
    return 0;
}

int fix(avlNode **root) {
    int lheight = 0;
    int rheight = 0;
    if ((*root)->l != NULL) {
        lheight = height((*root)->l);
    }
    if ((*root)->r != NULL) {
        rheight = height((*root)->r);
    }
    if (lheight - rheight == -1 || lheight - rheight == 1 || lheight - rheight == 0) {
        return 0;

    } else {
        if (lheight < rheight) {
            return rotate(root, 0);

        } else {
            return rotate(root, 1);
        }
    }
}