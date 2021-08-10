/*
	1 2 3 4 5
	161718196
	152425207
	142322218
	131211109
*/
#include<stdio.h>
int main()
{
	int i,j,f=1,g=1,m;
	for (i=1;i<=5;i++)
	{
		if(i>1 && i<5)
		{
			//if(i%2==0)
			g=10+f;
			m=g;
			//else
			//g=5*i;
		}
		for(j=1;j<=5;j++)
		{
			if(i>=2 && j==5)
			{
				printf("%d ",f);
				f++;
			}
			else if(i==1)
			{
				printf("%d ",f);
				f++;
			}
			
			else
			{
				printf("%d",m);
				m++;
			}
			
		}
		printf("\n");
	}
}
