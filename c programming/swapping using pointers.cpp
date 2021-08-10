#include<stdio.h>
//#include<conio.h>
void swappointer(int*,int*);
int main()
{
	int a,b,*pa,*pb;
	printf("enter two numbers : ");
	scanf("%d%d",&a,&b);
	pa=&a;
	pb=&b;
	swappointer(pa,pb);
	printf("values after swapping : \n    a=%d    b=%d",a,b);
}
void swappointer(int *pa,int *pb)
{
	int t;
	t=*pa;
	*pa=*pb;
	*pb=t;
}
