#include<stdio.h>
int a,b;
void swapglobal();
int main()
{
	printf("enter 2 no. : ");
	scanf("%d%d",&a,&b);
	printf("before swapping : \n    a=%d    b=%d",a,b);
	swapglobal();
	printf("\nafter swapping : \n    a=%d    b=%d",a,b);
	return 1;
}
void swapglobal(void)
{
	int t;
	t=a;
	a=b;
	b=t;
}
