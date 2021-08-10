#include <stdio.h>
int main()
{
	int r,c,s[4][4],k ;
	int a[4][4]=
	{
		{0,0,0,0},
		{1,1,1,1},
		{2,2,2,2},
		{3,3,3,3}
	};
	int b[4][4]=
	{
		{1,1,1,1},
		{2,2,2,2},
		{3,3,3,3},
		{4,4,4,4}
	};
	for(r=0;r<4;r++)
	{
		for(c=0;c<4;c++)
		{
			s[r][c]=0;
			
			for(k=0;k<4;k++)
			{
				s[r][c]=s[r][c]+(a[r][k]*b[k][c]);	
			}	
		}
	}
	
	for(r=0;r<4;r++)
	{
		for(c=0;c<4;c++)
		{
			printf("%d  ",s[r][c]);
		}
		printf("\n");
	}
	
	return 0;
}
