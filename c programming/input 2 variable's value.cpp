#include<stdio.h>
int main()
{
	int add,sub,mult,div;
	int a,b;
	
	printf("enter 2 no. on which you want to perform mathematical operation : \n");
	scanf("%d%d",&a,&b);
	
	add=a+b;
	sub=a-b;
	mult=a*b;
	div=a/b;
	
	printf("add : %d + %d = %d\n",a,b,add);
	printf("sub : %d - %d = %d\n",a,b,sub);
	printf("mult : %d * %d = %d\n",a,b,mult);
	printf("div : %d / %d = %d\n",a,b,div);
	
	return 0;
	}
