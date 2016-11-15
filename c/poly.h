
#ifndef __POLY_H__
#define __POLY_H__

#include "alist.h"

typedef struct PolyItem {
    float coef; // 系数
    int expn; // 指数
} PolyItem;

AList* createPoly();
void releasePoly();
void addPoly(AList* a, Alist* b);
void printPoly();
#endif
