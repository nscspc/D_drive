#include<stdio.h>
int main()
{
	int n,i,remain,a,digit[4],c;
	printf("enter the value in decimal that you want to convert in binary : ");
	scanf("%d",&n);
	a=n;
	for(i=0;i<4;i++)
	{
		//if (a>=2)
		//{
			remain=a%2;
			a=a/2;
			digit[i]=remain;
			c++;
		/*}
		else
		i=1;*/
	}
	for(i=0;i<c;i++)
	{
		printf("%d",digit[i]);
	}
}
