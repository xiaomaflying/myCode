
#include <stdio.h>
#include <stdlib.h>
#include "alist.h"
#include "poly.h"


AList* createPoly(void){
    AList* poly = initList();
    return poly;
}

void appendPolyItem(AList* poly, float coef, int expn){
    PolyItem* item = (PolyItem*)malloc(sizeof(PolyItem));
    item->coef = coef;
    item->expn = expn;
    
    ANode* node = (ANode*)malloc(sizeof(ANode));
    node->value = item;
    node->next = NULL;

    appendList(poly, node);
}


int main(){
    AList* poly = createPoly();
    appendPolyItem(poly, 2.4, 1);
    printf("hello\n");
    return 0;
}
