//BUBBLE SORTING.

#include<stdio.h>
int main()
{
	int i,j,n,temp;
	printf("enter no. of elements do you want to enter in the array : ");
	scanf("%d",&n);
	int a[n];
	printf("enter elements : ");
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
	}
	printf("elements before sorting : ");
	for(i=0;i<n;i++)
	{
		printf("%d ",a[i]);
	}
	
	for(j=0;j<n;j++)
	for(i=0;i<n-1;i++)
	{
		if(a[i]>a[i+1])
		{
			temp=a[i];
			a[i]=a[i+1];
			a[i+1]=temp;
		}
	}
	
	printf("\nelements after sorting : ");
	for(i=0;i<n;i++)
	{
		printf("%d ",a[i]);
	}
}
