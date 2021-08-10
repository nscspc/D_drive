#include <stdio.h>
int main()
{
	int  l,n,m=1;
	for(l=1;l<=5;l++)//outer loop represents rows.
	{
		for(n=1;n<=m;n++)//inner loop represents columns.
		{
			printf("%d",n);//statements in inner loop represents intersection in rows and columns or outer loop and inner loop.
		}
		printf("\n");
		m++;
	}	
	
}
