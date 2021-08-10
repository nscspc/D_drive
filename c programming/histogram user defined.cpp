#include<stdio.h>
int main()
{
	int i,j,k,n,value[20];
	char ylabels[20][10];
	printf("enter no. of elements : ");
	scanf("%d",&n);
	
	for(i=0;i<n;i++)
	{
		printf("enter label : ");
		scanf("%s",ylabels[i]);
		printf("enter integer values of the elements : ");
		scanf("%d",&value[i]);
	}
	for(i=0;i<n;i++)
	{
		for(j=0;j<3;j++)
		{
			//printf("%9c",'|');
			if(j%2!=0)
			{
				printf("%12s |",ylabels[i]);
			}
			else
			printf("%14c",'|');
			for(k=0;k<value[i];k++)
			{
				printf("*");
			}
			if(j%2!=0)
				printf("(%d)",value[i]);
			
			printf("\n");
		}
		printf("%14c\n",'|');
		
	}
}
