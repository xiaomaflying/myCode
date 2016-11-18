
#ifndef __POLY_H__
#define __POLY_H__

#include "alist.h"

typedef struct PolyItem {
    float coef; // 系数
    int expn; // 指数
} PolyItem;

AList* createPoly();
void releasePoly();
void appendPolyItem(AList* l, float coef, int expn);
void addPoly(AList* a, AList* b);
void printPoly();
#endif
