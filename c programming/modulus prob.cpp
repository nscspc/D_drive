#include<stdio.h>
main()
{
	int a,b,add,sub,prod,div;
	int mod;
	printf("enter 1st value = ");
	scanf("%d",&a);
	printf("enter 2nd value = ");
	scanf("%d",&b);
	add=a+b;
	sub=a-b;
	prod=a*b;
	div=a/b;
	mod=a%b;
	printf("add :- %d + %d = %d \n",a,b,add);
	printf("sub :- %d - %d = %d \n",a,b,sub);
	printf("prod :- %d * %d = %d \n",a,b,prod);
	printf("div :- %d / %d = %d \n",a,b,div);
	printf("mod :- %d '%' %d = %d \n",a,b,mod);
	printf("%");
	return 0;
}
