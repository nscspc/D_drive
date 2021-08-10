//BUBBLE SORTING using pointer.

#include<stdio.h>
int main()
{
	int i,j,n,temp ,*p;
	printf("enter no. of elements do you want to enter in the array : ");
	scanf("%d",&n);
	int a[n];
	
	p=&a[0];
	
	printf("enter elements : ");
	
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
	}
	printf("elements before sorting : ");
	
	for(i=0;i<n;i++)
	{
		printf("%d ",*(p+i));
	}
	
	for(j=0;j<n;j++)
	for(i=0;i<n-1;i++)
	{
		if(*p>*(p+1))
		{
			temp=*p;
			*p=*(p+1);
			*(p+1)=temp;
		}
	}
	
	printf("\nelements after sorting : ");
	for(i=0;i<n;i++)
	{
		printf("%d ",*(p+i));
	}
}
