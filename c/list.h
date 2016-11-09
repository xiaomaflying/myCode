
#define OK 0
#define ERROR -1
#define INIT_LIST_ERROR 1

typedef char* ElemType;

typedef struct Node{
    ElemType data;
    struct Node* next;
} Node;
