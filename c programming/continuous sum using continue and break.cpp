#include<stdio.h>
int main()
{
	int n,sum=0;
	
	while(1==1)
	{
		printf("enter no. : ");
		scanf("%d",&n);
		if (n<0)
		{
			continue;
		}
		if (n==0)
		{
			break;
		}
		sum=sum+n;
		printf("%d\n",sum);
	}
	return 0;
}
