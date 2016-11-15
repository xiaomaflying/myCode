
#include <stdio.h>
#include <stdlib.h>
#include "alist.h"

AList* initList(void){
    AList* list = (AList*)malloc(sizeof(AList));
    list->len = 0;
    list->head = (ANode*)malloc(sizeof(ANode));
    list->head->next = list->head->value = NULL;

    list->free = NULL;
}

