#include<stdio.h>
int main()
{
	float a,b;
	int add,sub,prod;
	float div;
	printf("enter 1st value = ");
	scanf("%f",&a);
	printf("enter 2nd value = ");
	scanf("%f",&b);//escape  sequences are not used in scanf() function
	add=a+b;
	sub=a-b;
	prod=a*b;
	div=a/b;
	printf("add :- %f + %f = %d \n",a,b,add);//type casting
	printf("sub :- %f - %f = %d \n",a,b,sub);
	printf("prod :- %f * %f = %d \n",a,b,prod);
	printf("div :- %f / %f = %f \n",a,b,div);
	return 0;
}

