#include<stdio.h>
int fact=1;
int f(int n)
{
	if(n>0){
	
	fact=fact*n*f(n-1);
	return fact;
	}else
	return 1;
}
int main()
{
	int n;
	scanf("%d",&n);
	printf("%d",f(n));
	return 0;
}
