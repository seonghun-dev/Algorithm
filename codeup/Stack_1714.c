#include <stdio.h>
#include <string.h>
#include "ListBaseStack.h"
#include "ListBaseStack.c"

int main() {
    char number[500];
    scanf("%s",number);

    Stack stack;
    StackInit(&stack);

    int sizeofstr = strlen(number); //문자열이 들어 있는 배열의 끝 번호 확인
    for (int i=0; i<sizeofstr ; i++) {
        SPush(&stack, number[i]);
    }

    while(!SIsEmpty(&stack))
        printf("%c", SPop(&stack));

    return 0;
}