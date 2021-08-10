#include<stdio.h>
int main()
{
	int i,j,k,value[5]={10,5,9,8,4};
	for(i=0;i<5;i++)
	{
		for(j=0;j<3;j++)
		{
			//printf("%9c",'|');
			if(j%2!=0)
			{
				printf("group %d |",i+1);
			}
			else
			printf("%9c",'|');
			for(k=0;k<value[i];k++)
			{
				printf("*");
			}
			if(j%2!=0)
				printf("(%d)",value[i]);
			
			printf("\n");
		}
		printf("%9c\n",'|');
		
	}
}
