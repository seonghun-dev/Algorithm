#include<stdio.h>

int main(){
    int n,sum=0;
    scanf("%d",&n);
    for(;n > 0;n--)
    sum += n;
    printf("%d\n",sum);
    return 0;
}