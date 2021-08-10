/*
	1
	3 2
	4 5 6
	10 9 8 7
	11 12 13 14 15
*/
#include<stdio.h>
int main()
{
	int i,j,k=0,n;
	printf("enter no. of rows : ");
	scanf("%d",&n);
	for(i=1;i<n;i++)
	{
		if(i%2==0)
		{
			for(int x=0;x<i;x++)
			{
				printf("%d ",k+i-x);
			}
			k+=i;
			}
		else
			for(j=1;j<=i;j++)
			{
				k++;
				printf("%d ",k);
			}
		printf("\n");
	}
}
