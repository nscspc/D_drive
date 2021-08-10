#include<stdio.h>
int main()
{
	int a,b;
	for(a=1;a<20;a++)
	{
		for(b=1;b<16;b++)
		{
			if(((a>=1 && a<4) || (a>=10 && a<=12)) || (a<=17 && a<=19))
			{
				printf("* ");
			}
			else if((a>=4 && a<10) && (b>=1 && b<=3))
			{
				printf("* ");
			}
			else if((a>=13 && a<=16) && (b>=12 && b<=15))
			{
				printf("* ");
			}
			else
			{
				printf(" ");
			}
		}
		printf("\n");
	}
}
