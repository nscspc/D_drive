#include <stdio.h>
int main()
{
	int n,pow,l=1,result=1;
	
	printf("enter no. : ");
	scanf("%d",&n);
	printf("enter power : ");
	scanf("%d",&pow);
	
	do
	{
		result=result*n;
		l++;
	}while(l<=pow);
	
	printf("%d",result);
	
	return 0;

}
