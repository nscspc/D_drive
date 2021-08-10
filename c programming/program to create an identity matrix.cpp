#include <stdio.h>
int main()
{
	int r,c;
	int m[3][3];
	
	for(r=0;r<3;r++)
	{
		for(c=0;c<3;c++)
		{
			if (r==c)
			{
				m[r][c]=1;
			
			}
			else
			{
				m[r][c]=0;
			}
		}
	}
	
	for(r=0;r<3;r++)
	{
		for(c=0;c<3;c++)
		{
			printf("%d",m[r][c]);
		}
		printf("\n");
	}
	
	return 0;
}
