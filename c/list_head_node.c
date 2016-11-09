
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define OK 0
#define ERROR -1
#define INIT_LIST_ERROR 1

typedef char* ElemType;

typedef struct Node{
    ElemType data;
    struct Node* next;
} Node;

typedef struct List{
    Node* head;

    /* Operations */
    void (*free)(struct List* self);
    void (*append)(struct List* self, Node* node);
    void (*insert)(struct List* self, Node* node, int pos);
    Node* (*get)(struct List* self, int pos);
    void (*delete)(struct List* self, int pos);
    void (*print)(struct List* self);
} List;


/* Node opertions */
Node* initStringNode(char* data){
    Node* node = (Node*)malloc(sizeof(Node));
    node->data = data;
    node->next = NULL;
    return node;
}

void freeNode(Node* node){
    //if (node->data != NULL) free(node->data);
    free(node);
}

void printNode(Node* node){
    printf("<Node %o data %s>", node, node->data);
}


/* List operations */

/* Base operations */
void freeList(List* self){
    // Free the main body of list
    Node* cur = self->head->next;
    Node* tmp;
    while(cur){
        tmp = cur;
        cur = cur->next;
        freeNode(tmp);
    }

    // Free list head node and list itself
    free(self->head);
    free(self);
}

void appendNode(List* self, Node* node){
    // Traverse the list to the last node
    Node* cur = self->head;
    while(cur->next){
        cur = cur->next;
    }

    cur->next = node;
    node->next = NULL;
}

void insertNode(List* self, Node* node, int pos){
    int cur_post = 0;
    Node* cur = self->head;
    while(cur_post < pos){
        if (!cur->next) return;
        cur = cur->next;
        cur_post += 1;
    }
    
    node->next = cur->next;
    cur->next = node;
}

Node* getNode(List* self, int pos){
    int cur_post = 0;
    Node* cur = self->head;
    while(cur_post < pos){
        if (!cur->next) return NULL;
        cur = cur->next;
        cur_post += 1;
    }
    return cur;
}

void deleteNode(List* self, int pos){
    if (pos < 1) return;
    int cur_pos = 0;
     
    Node* cur = self->head;
    Node* pre;

    while(cur_pos < pos){
        if (!cur->next) return;
        pre = cur;
        cur = cur->next;
        cur_pos += 1;
    }

    pre->next = cur->next;
    freeNode(cur);
}

void printList(List* self){
    Node* cur = self->head->next;
    while(cur){
        printf("<Node %o data %s> --> ", cur, cur->data);
        cur = cur->next;
    }
    printf("NULL\n");
}


// Init List: malloc memory; init List base operations

List* initList(){
    // Malloc memory for List and it's head Node
    List* list = (List*)malloc(sizeof(List));
    list->head = (Node*)malloc(sizeof(Node));
    list->head->next = NULL;

    // Init List base operations
    list->free = freeList;
    list->append = appendNode;
    list->insert = insertNode;
    list->get = getNode;
    list->delete = deleteNode;
    list->print = printList;

    return list;
}


/* Test for operations */

// Help functions for test
char* assertEqual(void* a, void* b){
    if (a == b) return "True";
    else return "False";
}

void testBaseFunctions(){
    // Test init & print
    List* list = initList();
    list->print(list);

    // Test append
    Node* node1 = initStringNode("Hello");
    Node* node2 = initStringNode("world");
    list->append(list, node1);
    list->append(list, node2);
    list->print(list);

    // Test insert
    Node* node3 = initStringNode("Hi");
    Node* node4 = initStringNode("China");
    list->insert(list, node3, 0);
    list->insert(list, node4, 1);
    list->print(list);

    Node* node5 = initStringNode("!");
    Node* node6 = initStringNode("Error");
    list->insert(list, node5, 4);
    list->insert(list, node6, 6);
    list->print(list);

    // Test get
    printf("%s\n", assertEqual(list->get(list, 1), node3));
    printf("%s\n", assertEqual(list->get(list, 5), node5));
    printf("%s\n", assertEqual(list->get(list, 0), node6));

    // Test delete
    list->delete(list, 0); // no work
    list->delete(list, 1);
    list->delete(list, 4);
    list->print(list);

    // Test free
    list->free(list);
}


int main(){
    testBaseFunctions();

    //int a = 2;
    //void* p = &a;
    //printf("%d\n", *(int *)p); 
}
