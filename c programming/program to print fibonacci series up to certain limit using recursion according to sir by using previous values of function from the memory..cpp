//program to print fibonacci series up to certain limit using recursion according to sir by using previous values of function from the memory.

#include<stdio.h>

int fibo(int);

int main()
{
	int i,n;
	printf("enter no. : ");
	scanf("%d",&n);
	
	if (n>=1)
	printf("%d",0);
	
	for(i=0;i<n-1;i++)
	{
		printf("%d",fibo(i));
	}
}

int fibo(int n)
{
	if (n>=2)
	{
		return fibo(n-2)+fibo(n-1);
	}
	else
	return 1;
}
