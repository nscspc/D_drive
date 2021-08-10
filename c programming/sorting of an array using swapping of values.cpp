#include<stdio.h>
int main()
{
	int n,i,j,tmp;
	printf("enter n : ");
	scanf("%d",&n);
	int a[n];
		for(j=0;j<n;j++)
		scanf("%d",&a[j]);	
	for(j=0;j<n;j++)
	for(i=0;i<n;i++)
	{
		
		if(a[i]>a[i+1])
		{
			tmp=a[i];
			a[i]=a[i+1];
			a[i+1]=tmp;
		}
		
	}
	for(j=0;j<n;j++)
		printf("%d",a[j]);	
}
