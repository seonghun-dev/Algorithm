#include <stdio.h>
#include "ListBaseStack.h"
#include "ListBaseStack.c"

int main() {
    int n = 0;
    int temp;
    scanf("%d", &n);

    Stack stack;
    StackInit(&stack);

    for (int i = 0; i < n; i++) {
        scanf("%d",&temp);
        SPush(&stack, temp);
    }

    while(!SIsEmpty(&stack))
        printf("%d ", SPop(&stack));

    return 0;
}