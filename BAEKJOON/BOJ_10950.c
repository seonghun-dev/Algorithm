#include<stdio.h>

int main(){
    int n;
    int c=0;
    scanf("%d",&n);
    int a[n],b[n];
    for(;c<n;c++)
    scanf("%d %d",&a[c],&b[c]);
    for(c=0;c<n;c++)
    printf("%d\n",a[c] + b[c]);
    return 0;
}