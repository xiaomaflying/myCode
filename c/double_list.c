#include <stdio.h>
#include <stdlib.h>
#include "double_list.h"

/* Help functions */
void printDNode(DNode* node){
    if (node == NULL){
        printf("NULL\n");
        return;
    }
    printf("<DNode %o %s>\n", node, node->data);
}

DNode* initDNode(char* data){
    DNode* node = (DNode*)malloc(sizeof(DNode)); 
    node->data = data;
    node->next = NULL;
    return node;
}

void printDNodePrev(DNode* node){
    printDNode(node->prev);
}

/* Prototypes */
DList* dlInit(void){
    DList* list = (DList*)malloc(sizeof(DList));
    list->head = (DNode*)malloc(sizeof(DNode));
    list->head->next = list->head->prev = NULL;
    list->tail = list->head;
    list->length = 0;
}

void dlFree(DList* list){
    dlClear(list);
    free(list->head);
    free(list);
}

void dlPrint(DList* list){
    printf("<DList length %d>  ", dlLength(list));
    DNode* cur = list->head->next;
    while(cur){
        printf("<DNode %o %s> <--> ", cur, cur->data);
        cur = cur->next;
    }
    printf("NULL\n");
}

void dlClear(DList* list){
    DNode* cur = list->tail;
    while(cur != list->head){
        cur = cur->prev;
        free(cur->next);
        cur->next = NULL;
    }
    list->tail = list->head;
    list->length = 0;
}

void dlAppend(DList* list, DNode* node){
    list->tail->next = node;
    node->prev = list->tail;
    node->next = NULL;
    list->tail = node;
    list->length += 1;
}

void dlInsertItem(DList* list, DNode* node, int pos){
    int cur_pos = 0;
    DNode* cur = list->head;
    while(cur_pos < pos){
        if (cur->next == NULL) return;
        cur_pos += 1;
        cur = cur->next;
    }

    if (cur == list->tail){
        cur->next = node;
        node->prev = cur;
        node->next = NULL;
        list->tail = node;
    }
    else{
        node->next = cur->next;
        node->prev = cur;
        cur->next->prev = node;
        cur->next = node;
    }
    list->length += 1;
}

void dlDeleteItem(DList* list, int pos){
    if (pos < 1) return;

    int cur_pos = 0;
    DNode* cur = list->head;
    while(cur_pos < pos){
        if (cur->next == NULL) return;
        cur_pos += 1;
        cur = cur->next;
    }

    if(cur == list->tail){
        cur->prev->next = NULL;
        list->tail = cur->prev;
        free(cur);
    }
    else{
        cur->prev->next = cur->next;
        cur->next->prev = cur->prev;
        free(cur);
    } 

    list->length -= 1;
}

DNode* dlGetItem(DList* list, int pos){
    int cur_pos = 0;
    DNode* cur = list->head;
    while(cur_pos < pos){
        if (cur->next == NULL) return NULL;
        cur_pos += 1;
        cur = cur->next;
    }

    return cur;
}

void dlTraverse(DList* list, visitItem* visit){
    DNode* cur = list->head->next;
    while(cur){
        visit(cur);
        cur = cur->next;
    }
}

int dlEmpty(DList* list){
    if (list->head == list->tail) return DL_EMPTY;
    return DL_NO_EMPTY;
}

int dlLength(DList* list){
    return list->length;
}

/* Test for prototypes */
void testPrototypes(){
    DList* list = dlInit();
    printf("%d\n", dlEmpty(list));
    dlPrint(list);

    DNode* node1 = initDNode("Hello");
    DNode* node2 = initDNode("world");

    dlAppend(list, node1);
    dlAppend(list, node2);
    dlPrint(list);

    dlClear(list);
    dlPrint(list);
    dlFree(list);

    /* Test dlInsertItem */

    DList* list1 = dlInit();
    DNode* node3 = initDNode("Hello");
    DNode* node4 = initDNode("world");

    dlInsertItem(list1, node3, 0);
    dlInsertItem(list1, node4, 1);
    dlPrint(list1);
    printDNodePrev(node4);
    printDNodePrev(node3);
    printf("dlTraverse-->");
    dlTraverse(list1, printDNode);
    printf("\n");

    /* Test dlDeleteItem & dlGetItem */
    printDNode(dlGetItem(list1, 1));
    printDNode(dlGetItem(list1, 2));
    dlDeleteItem(list1, 1);
    dlPrint(list1);

    printDNode(dlGetItem(list1, 1));
    dlDeleteItem(list1, 1);
    dlPrint(list1);

    printDNode(dlGetItem(list1, 1));
}


int main(){
    testPrototypes();
}
