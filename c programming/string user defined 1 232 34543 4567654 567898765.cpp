/*

        1
      2 3 2
    3 4 5 4 3
  4 5 6 7 6 5 4
5 6 7 8 9 8 7 6 5

*/
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int main()
{
	char input[100];
	printf("enter string : ");
	scanf("%s",input);
	
	int nr,l=strlen(input);
	if(l%2!=0)
	{
		nr=(l/2)+1; 
	}
	else
	{
		nr=l/2;
	}
	int i,j,k,x,a=0,b=0;
	for(i=0;i<nr;++i)
	{
		for(j=0;j<nr*2-2-a+25;++j)
		{
			printf(" ");
		}
		for(k=i;k<=i+b;++k)
		{
			printf("%c ",input[k]);
		}
		for(x=k-2;x>=i;--x)
		{
			printf("%c ",input[x]);
		}
		printf("\n");
		a+=2;
		b++;
	}
}
