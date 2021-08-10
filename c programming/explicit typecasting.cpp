#include<stdio.h>
int main()
{
	int add,sub,mult;
	int a,b;
	float div;
	printf("enter 2 no. on which you want to perform mathematical operation : \n");
	scanf("%d%d",&a,&b);
	
	add=a+b;
	sub=a-b;
	mult=a*b;
	div=(float)a/b;//explicit type casting :- In this type of type casting we have to change the datatype manually , and the datatype gets changed temporarily (not permanently).
	printf("add : %d + %d = %d\n",a,b,add);
	printf("sub : %d - %d = %d\n",a,b,sub);
	printf("mult : %d * %d = %d\n",a,b,mult);
	printf("div : %d / %d = %f\n",a,b,div);
	printf("%d %d",a,b);
	
	return 0;
}
