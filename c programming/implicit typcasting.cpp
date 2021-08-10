#include<stdio.h>
int main()
{
	float a,b;
	int add,sub,prod,div;
	int mod;
	printf("enter 1st value = ");
	scanf("%f",&a);//scanf("format specifiers",&{address of}variable)
	printf("enter 2nd value = ");
	scanf("%f",&b);
	add=a+b;//result is in 
	sub=a-b;
	prod=a*b;
	div=a/b;
	mod=(int)a%(int)b;// explicit typecasting for both variables as one int can change the dattype of only one variable
	printf("add :- %f + %f = %f\n",a,b,add);
	printf("sub :- %f - %f = %f\n",a,b,sub);
	printf("prod :- %f * %f = %f\n",a,b,prod);
	printf("div :- %f / %f = %f\n",a,b,div);
	printf("mod :- %f %f = %d",a,b,mod);
	return 0;
}

