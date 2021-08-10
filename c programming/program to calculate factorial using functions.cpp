#include<stdio.h>

int fact(int n);

int main()
{
	int n;
	printf("enter the no. of which you want to calculate factorial : ");
	scanf("%d",&n);
	
	printf("%d",fact(n));
}
int fact(int n)
{
	int fact=1,i;
	
	for(i=0;i<n;i++)
	{
		fact=fact*(n-i);
		
	}
	return fact;
}
