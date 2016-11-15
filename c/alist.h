/* alist.h - A generic single linked list implementation with head node. 
 *
 */

#ifndef __ALIST_H__
#define __ALIST_H__

typedef struct ANode {
    void* value;
    struct ANode* next;
} ANode;

typedef struct AList {
    ANode* head;
    int len;

    void (*free)(void* ptr); /* Used to free the value in the node */
} AList;

AList* initList(void);
void releaseList(AList* list);
void printList(AList* list);

#endif
