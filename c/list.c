#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "list.h"


typedef struct List{
    Node* head;

    /* Operations */
    void (*free)(struct List* self);
    void (*append)(struct List* self, Node* node);
    int (*insert)(struct List* self, Node* node, int pos);
    Node* (*get)(struct List* self, int pos);
    void (*delete)(struct List* self, int pos);
    void (*print)(struct List* self);
} List, SingleList;

void printNode(Node* node){
    if (!node) {
        printf("<Node %o>: %s\n", node, "NULL");
        return;
    }
    printf("<Node %o>: %s\n", node, node->data);
}


/* SingleList operations */

/* Base operations*/
void freeSingleList(SingleList* self){
    /* Free SingleList memory */
    Node* cur = self->head;
    while(cur){
        Node* tmp = cur;
        cur = cur->next;
        free(tmp);
    }
    free(self);
}

void appendNode(SingleList* list, Node* node){
    Node* cur = list->head;
    if (!cur){
        list->head = node;
        return;
    }
    Node* pre;
    while(cur){
        pre = cur;
        cur = cur->next;
    }
    pre->next = node;
    node->next = NULL;
}

int insertNode(SingleList* list, Node* node, int pos){
    if (pos == 0){
        if (list->head){
            node->next = list->head;
            list->head = node;
        }
        else {
            list->head = node;
            node->next = NULL;
        }
        return OK;
    }
    
    int cur_pos = 1;
    Node* cur = list->head;
    while(cur_pos < pos){
        if (!cur->next) return ERROR;
        cur = cur->next;
        cur_pos += 1;
    }

    node->next = cur->next;
    cur->next = node;
    return OK;
}

Node* getNode(SingleList* list, int pos){
    if (!list->head) return NULL;

    int cur_pos = 0;
    Node* cur = list->head;

    while(cur_pos < pos){
        if (!cur->next) return NULL;
        cur_pos += 1;
        cur = cur->next;
    }
    return cur;
}

void deleteNode(SingleList* list, int pos){
    if (!list->head) return;

    Node* cur = list->head;
    Node* pre = cur;

    if (pos == 0){
        list->head = list->head->next;
        free(cur);
        return;
    } 

    int cur_pos = 0;
    while(cur_pos < pos){
        if (!cur->next) return;
        cur_pos += 1;
        pre = cur;
        cur = cur->next;
    }
    
    pre->next = cur->next;
    free(cur);
}

void printSingleList(SingleList* list){
    Node* cur = list->head;
    while(cur){
        printf("<Node %o %s> -> ", cur, cur->data);
        cur = cur->next;
    }
    printf("NULL\n");
}

SingleList* newSingleList(){
    /* Malloc SingleList memory */
    SingleList* list = (SingleList*)malloc(sizeof(SingleList));
    list->head = NULL;

    list->free = freeSingleList;
    list->append = appendNode;
    list->insert = insertNode;
    list->get = getNode;
    list->delete = deleteNode;
    list->print = printSingleList;
    return list;
}


/* Other operations*/
int initListWithNodes(List* list, Node** nodes, int length){
    /* Init SingleList with Node pointer array */
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

void createListByInput(SingleList* list, int n){
    printf("n is %d\n", n);
    int size = 1024; // buffer
    char buffer[size];
    if (list->head || n == 0) return;
    list->head = (Node*)malloc(sizeof(Node));
    fgets(buffer, size, stdin);
    char* data = (char*)malloc(strlen(buffer));
    strncpy(data, buffer, strlen(buffer));
    data[strlen(buffer)-1] = '\0';  // remove the '\n' from stdin
    list->head->data = data;
    list->head->next = NULL;

    Node* cur = list->head, *tmp;
    int i=1;
    for(; i<n; i++){
        tmp = (Node*)malloc(sizeof(Node));
        tmp->next = NULL;

        fgets(buffer, size, stdin);
        char* data = (char*)malloc(strlen(buffer));
        strncpy(data, buffer, strlen(buffer));
        data[strlen(buffer)-1] = '\0';
        tmp->data = data;

        cur->next = tmp;
        cur = cur->next;
    }
}

SingleList* mergeSeqLists(List* list1, List* list2){

}


/* Test cases */
void testBaseFunctions(){
    printf("Test newSingleList, print functions...\n");
    SingleList* list = newSingleList();
    list->print(list);
    
    printf("Test append, insert functions...\n");
    Node* node1 = (Node*)malloc(sizeof(Node));
    Node* node2 = (Node*)malloc(sizeof(Node));
    node1->data = "Hello";
    node1->next = NULL;
    node2->data = "World";
    node2->next = NULL;
    list->append(list, node1);
    list->insert(list, node2, 1);

    printf("Test get function...\n");
    printNode(list->get(list, 1));
    printNode(list->get(list, 3));

    printf("Test delete function...\n");
    list->print(list);
    list->delete(list, 0);
    list->print(list);

    printf("Test free function...\n");
    list->free(list);
}

void testExtendFunctions(){
    SingleList* list = newSingleList();
    int num;
    printf("Please input the number of list:\n");
    scanf("%d\n", &num);
    createListByInput(list, num);
    list->print(list);
}


int main(){
    //testBaseFunctions();
    testExtendFunctions();
    //char data[100];
    //char* dest;
    //int size = 1024;
    //fgets(data, size, stdin);
    //printf("your input is : %s, length is %d\n", data, strlen(data));
    //dest = (char*)malloc(strlen(data));
    //strncpy(dest, data, strlen(data));
    //dest[strlen(data)-1] = '\0';
    //printf("%s", dest);
}
