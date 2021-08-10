#include<stdio.h>

int fact(int n);
int i=0;
int fac=1;
int main()
{
	int n;
	printf("enter the no. of which you want to calculate factorial : ");
	scanf("%d",&n);
	
	printf("%d",fact(n));
}
int fact(int n)
{
	if (i!=n)
	{
		fac=fac*(n-i);
		i++;
		fact(n);
	}
	return fac;
}
