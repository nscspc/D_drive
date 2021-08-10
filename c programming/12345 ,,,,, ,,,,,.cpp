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
	int i,j,f=1,a[5][5];
	for (i=0;i<5;i++)
	{
		for(j=0;j<5;j++)
		{
			if(i==0 || j==4)
			{
				a[i][j]=f;
				f++;
			}
		//	f++;
			if(i==4 && j==4-1)
			{
				a[i][j]=f;
				//for(int x=0)
			}
			
		}
		printf("\n");
	}
}
