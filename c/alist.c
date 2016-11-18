
#include <stdio.h>
#include <stdlib.h>
#include "alist.h"

AList* initList(void){
    AList* list = (AList*)malloc(sizeof(AList));
    list->len = 0;
    list->head = (ANode*)malloc(sizeof(ANode));
    list->head->next = list->head->value = NULL;

    list->free = NULL;
    list->print = NULL;
}

void releaseList(AList* list){
    ANode* tmp;
    while(list->head->next){
        tmp = list->head->next->next;
        if (list->free){
            list->free(list->head->next->value);
        }
        else {
            free(list->head->next->value);
        }
        free(list->head->next);
        list->head->next = tmp;
    }

    free(list->head);
    free(list);
}

void printList(AList* list){
    ANode* current = list->head->next;
    while(current){
        if (list->print){
            list->print(current->value);
        }
        else {
            printf("%o", current); 
        }
        printf(" --> ");
        current = current->next;
    }
    printf("NULL");
}

void appendList(AList* list, ANode* node){
    ANode* current = list->head;
    while(current->next){
        current = current->next;
    }
    current->next = node;
    node->next = NULL;
}

