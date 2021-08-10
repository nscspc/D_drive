#include<stdio.h>
int main()
{
	float a,b,add,sub,prod,div;
	int mod;
	printf("enter 1st value = ");
	scanf("%f",&a);//scanf("format specifiers",&{address of}variable)
	printf("enter 2nd value = ");
	scanf("%f",&b);
	add=a+b;
	sub=a-b;
	prod=a*b;
	div=a/b;
	mod=a%b;//mod operator cannot be used with float value
	printf("add :- %f + %f = %f",a,b,add);
	printf("sub :- %f - %f = %f",a,b,sub);
	printf("prod :- %f * %f = %f",a,b,prod);
	printf("div :- %f / %f = %f",a,b,div);
	printf("mod :- %f % %f = %d",a,b,mod);
	return 0;
}
