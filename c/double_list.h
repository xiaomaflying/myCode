/* Data structure double list with a head node and a tail pointer. 
 * Writen by Maxinmin.
 */

#ifndef __DLIST_H__
#define __DLIST_H__

#define ElemType char*

/* Status code */
#define DL_EMPTY 0
#define DL_NO_EMPTY 1

typedef struct DNode {
    ElemType data;
    struct DNode* prev;
    struct DNode* next;
} DNode;

typedef struct DList {
    DNode* head;
    DNode* tail;
    int length;
} DList;

/* Prototypes (`dl` is short for DoubleList) */

typedef void visitItem(DNode* node);

DList* dlInit(void);
void dlFree(DList* list);
void dlPrint(DList* list);
void dlClear(DList* list);
void dlAppend(DList* list, DNode* node);
void dlInsertItem(DList* list, DNode* node, int pos);
void dlDeleteItem(DList* list, int pos);
DNode* dlGetItem(DList* list, int pos);
void dlTraverse(DList* list, visitItem* visit);

int dlEmpty(DList* list);
int dlLength(DList* list);

#endif
