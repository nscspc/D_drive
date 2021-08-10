//program to add no. continuously untill 0 is pressed.
#include<stdio.h>
int main()
{
	int n1,n2,sum,i;
	printf("enter no. : ");
	scanf("%d",&n1);
	printf("enter no. : ");
	scanf("%d",&n2);
	sum=n2;
	for(i=1;i>0;i++)
	{
		sum=sum+n1;
		printf("result is : %d\n\n",sum);
		printf("enter no. : ");
		scanf("%d",&n1);
		if(n1==0)
		i=-1;
	}
	return 0;
}
