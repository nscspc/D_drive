#include<stdio.h>

int min(int[]);

int main()
{
	int i,j,tmp;
	int a[5]={1,4,3,0,5};
	for(i=0;i<5;i++)
	{
		for(j=0;j<5;j++)
		{
			tmp=a[i];
			if (tmp>a[j])
			{
				a[i]=a[j];
				a[j]=tmp;
			}
		}
		
	}
	for(i=0;i<5;i++)
	{
		printf("%d",a[i]);
	}
	return 0;
}
