#include <stdio.h>
#include <stdlib.h>

#define OK 0
#define INIT_LIST_ERROR 1

typedef struct Node{
    void* data;
    struct Node* next;
} Node;

typedef struct {
    Node* head;
} List, SingleList;

void printNode(Node* node){
    printf("<Node %o>: %s", (unsigned int)node, node->data);
}

int initListWithNodes(List* list, Node** nodes, int length){
    if (list->head) return INIT_LIST_ERROR;
    if (length == 0) return OK;
    int i;
    Node* cur = nodes[0];
    for(i=1; i<length; i++){
        cur->next = nodes[i];
        cur = cur->next;
    }
    cur->next = NULL;
    list->head = nodes[0];
    return OK;
}

void printSingleList(SingleList* list){
    Node* cur = list->head;
    while(cur){
        printf("<Node %o> %s", (unsigned int)cur, cur->data);
        cur = cur->next;
    }
}

int main(){
    Node* node = (Node*)malloc(sizeof(Node));
    node->data = "Hello world";
    node->next = NULL;
    //printNode(node);

    Node* node1 = (Node*)malloc(sizeof(Node));
    Node* node2 = (Node*)malloc(sizeof(Node));
    node1->data = "Hello";
    node2->data = "World";
    Node* nodes[2] = {node1, node2};
    SingleList* list = (SingleList*)malloc(sizeof(SingleList)) ;
    list->head = NULL;
    if (initListWithNodes(list, nodes, 2)){
        printf("init error");
        exit(0);
    }
    
    printSingleList(list);

    return 0;
}
