#include <stdio.h>
#include <stdlib.h>
#include "double_list.h"

/* Help functions */
void printDNode(DNode* node){
    if (node == NULL){
        printf("NULL\n");
    }
    printf("<DNode %o %s>\n", node, node->data);
}

DNode* initDNode(char* data){
    DNode* node = (DNode*)malloc(sizeof(DNode)); 
    node->data = data;
    node->next = NULL;
    return node;
}

/* Prototypes */
DList* dlInit(void){
    DList* list = (DList*)malloc(sizeof(DList));
    list->head = (DNode*)malloc(sizeof(DNode));
    list->head->next = list->head->prior = NULL;
    list->tail = list->head;
    list->length = 0;
}

void dlFree(DList* list){
    dlClear(list);
    free(list->head);
    free(list);
}

void dlPrint(DList* list){
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
        cur = cur->prior;
        free(cur->next);
        cur->next = NULL;
    }
    list->tail = list->head;
}

void dlAppend(DList* list, DNode* node){
    list->tail->next = node;
    node->prior = list->tail;
    node->next = NULL;
    list->tail = node;
}

void dlInsertItem(DList* list, DNode* node, int pos){}
void dlDeleteItem(DList* list, int pos){}
DNode* dlGetItem(DList* list, int pos){}
void dlTraverse(DList* list, visitItem* visit){}

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
}


int main(){
    testPrototypes();
}
