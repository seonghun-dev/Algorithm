#include<stdio.h>

int main(){
    int year, check4, check10, check40;
    scanf("%d", &year);
    if(0 == (year % 4))
    	if(( 0 != year % 100) || (0 == year % 400))
    	printf("1\n");
    	else
    	printf("0\n");
    else
    printf("0\n");
    return 0;
}