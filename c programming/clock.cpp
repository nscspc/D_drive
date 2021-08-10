#include<stdio.h>
int main()
{
	int i,j,k,a,b,c,d;
	printf("enter current time : ");
	scanf("%d:%d:%d",&i,&j,&k);
	for(d=0;d+i<=24;d++)
	{
		for(c=0;c+j<=60;c++)
		{
			for(a=1;a+k<=60;a++)
			{
				printf("%d:%d:%d",i+d,j+c,k+a);
				for(b=1;b<=362000050;b++);
				printf("\b\b\b\b\b\b\b\b");
			}
			k=0;
		}
	}		
}
