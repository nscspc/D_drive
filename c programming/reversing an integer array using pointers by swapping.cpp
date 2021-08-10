#include<stdio.h>
int main()
{
	int *p,a[100],n,t;
	
	printf("enter no. of elements : ");
	scanf("%d",&n);
	
	for(int i=0;i<n;i++)
	scanf("%d",&a[i]);
	p=a;

	for(int i=0;i<n/2;i++)
	{
		t=*(p+i);
		*(p+i)=*(p+n-1-i);
		*(p+n-1-i)=t;
	}
	
	printf("a[%d] = [ ",n);
	for(int i=0;i<n;i++)
	printf("%d ",a[i]);
	printf("]");
	
	return 0;
	
}
