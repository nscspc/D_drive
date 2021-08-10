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
				printf("%d ",1);
			
			}
			else
			{
				printf("%d ",0);
			}
		}
		printf("\n");
	}
	
	return 0;
}
