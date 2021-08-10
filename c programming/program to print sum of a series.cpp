//program to print sum of a series. 

#include<stdio.h>
int main()
{
	int n,x,i=0,j,pow,fact;
	float sum=0.0;
	printf("enter limit : ");
	scanf("%d",&n);
	printf("enter no. : ");
	scanf("%d",&x);
	
	do
	{
		pow=1;
		fact=1;
		
		if(i!=0)
		{
			for(j=1;j<=i;j++)
			{
				pow=pow*x;
			}
			for(j=i;j>0;j--)
			{
				fact=fact*j;
			}
			printf(" + (%d^%d / %d!)",x,i,i);
			sum=sum+((float)pow/fact);
		}
		else
		{
			sum=sum+1;	
			printf("%d",1);
		}
		
		i++;
		
	}while(i<=n);
	
	printf(" = %f",sum);
	return 0;
}
