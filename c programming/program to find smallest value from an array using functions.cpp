#include<stdio.h>

int min(int [],int);

int main()
{
	int i,n;
	printf("enter the no. of elements you want to enter in the array : ");
	scanf("%d",&n);
	int a[n];
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
	}
	
	min(a,n);
	return 0;
}

int min(int a[],int n)
{
	int i,j,tmp;

	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
		{
			tmp=a[i];
			if (tmp>a[j])
			{
				a[i]=a[j];
				a[j]=tmp;
			}
		}
		
	}
	
	for(i=0;i<n;i++)
	{
		printf("%d",a[i]);
	}

}
