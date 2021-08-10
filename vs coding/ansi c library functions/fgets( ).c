#include<stdio.h>
int main()
{
    char b;
    char a='c';
    FILE *f;
    f=fopen("fgets.txt","w");
    fputs(a,f);
    fgets(b,1,f);
    //int r=ispunct(a);
    rewind(f);
    printf("%c",b);
}