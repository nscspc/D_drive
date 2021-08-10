#include<stdio.h>

void swap(int,int);

int main()
{
	int a,b;
	printf("enter value of a : ");
	scanf("%d",&a);
	printf("enter value of b : ");
	scanf("%d",&b);
	
	printf("\nvalues before swapping : \n a = %d  ,  b = %d\n",a,b);
	swap(a,b);
	printf("\nvalues before swapping : \n a = %d  ,  b = %d",a,b);
	
}

void swap(int a,int b)
{
	int t;
	t=a;
	a=b;
	b=t;
}
