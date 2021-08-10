//program to print fibonacci series up to certain limit using recursion.

#include<stdio.h>

void fibo(int);

int a=0,b=1;

int main()
{
	int n;
	printf("enter no. : ");
	scanf("%d",&n);
	if (n==1)
	printf("%d",a);
	if (n>=2)
	{
		printf("%d , %d",a,b);
		fibo(n-2);
	}
}

void fibo(int s)
{
	if (s!=0)
	{
		int c;
		c=b+a;
		printf(" , %d",c);
		a=b;
		b=c;
		s--;
		fibo(s);
	}
}
