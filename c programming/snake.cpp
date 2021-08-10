#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
int main()
{
	int i,j,k,a,b,c=10;
	for(k=0;k<=5;k++)
	{
		for(i=0;i<=20;i++)
		{
			c=10;
			for(j=0;j<=20;j++)
			{	
				if(j==0 || j==20 || i==0 || i==20)
				{
					printf("* ");
				}
				else if(i==10 && j==10)
				{
					for(a=0;a<=k;a++)
					printf(" ");
					printf("**");
				}
				else if(i==10 && j==c+1)
				{
					printf(" ");
				}
				else
				{
					/*if(i==10 && j==c+1)
						printf("\0");
					else*/
						printf("  ");
				}
				
				if(c<=a+10)
				{	
					c++;
				}
			}
			/*if(c<=a+10)
			{
				c++;
			}*/
			
			printf("\n");
		}
		
		printf("\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b");
	}
}
