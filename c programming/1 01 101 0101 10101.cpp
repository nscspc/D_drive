#include<stdio.h>
int main()
{
	int r,c,n,no;
	
	printf("enter no. of rows : ");
	scanf("%d",&n);
	
	for(r=0;r<n;r++)
	{
		if(r%2==0)
		{
			no=1;
		}
		else
		{
			no=0;
		}
		for(c=0;c<=r;c++)
		{
			printf("%d ",no);
			if (no==1)
			{
				no=0;
			}
			else
			{
				no=1;
			}
		}
		
		printf("\n");
		
	}
	
}
