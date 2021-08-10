#include <stdio.h>
int main()
{
	int no,digit,n,sum=0;
	printf("enter no. : ");
	scanf("%d",&no);
	n=no;
	for(x=0;x<3;x++)
	{
		digit=n%10;
		n=no/10;
		sum=sum+(digit*digit*digit);
	}
	
	if(no==sum)
	{
		printf("%d is an ARMSTRONG NO.");
	}
	else
	{
		printf("%d is NOT an ARMSTRONG NO.");
	}
}
