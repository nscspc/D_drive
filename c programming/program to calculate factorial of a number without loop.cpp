//program to calculate factorial of a number without loop .

#include<stdio.h>

int fact(int);

int main()
{
	int n;
	printf("enter no. : ");
	scanf("%d",&n);
	printf("%d",fact(n));
}

int fact(int f)
{
	if(f>0)
	return f*fact(f-1);//5*4*3*2*1*1
	
	else if(f<0)
	printf("factorial of negative( - ) values is not determined .");
	//return f*fact(f-1); : -4 * -5 * -6 * -7*......
	
	else
	return 1;
}
