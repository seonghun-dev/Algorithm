#include<stdio.h>

int main(){
    int a,b,num1,num2,num3;
    scanf("%d %d", &a, &b);
    num1 = b % 10;
    num2 = b % 100 - num1;
    num3 = b-(num1 + num2);
    printf("%d\n", num1 * a);
    printf("%d\n", (num2 * a)/10);
    printf("%d\n", (num3 * a)/100);
    printf("%d\n", a*b);
    return 0;
}