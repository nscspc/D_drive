#include<stdio.h>
int main()
{
	int i=0,j,/*a[r][c],b[r][c],c[r][c]*/r,c;
	printf("enter no of rows and columns: ");
	scanf("%d%d",&r,&c);
	printf("enter elements of 1st matrix : ");
	int a[r][c]={0},b[r][c]={0},c[r][c]={0};
	while(i<r)
	{
		j=0;
		while(j<c)
		{
			scanf("%d",&a[r][c]);
			j++;
		}
		i++;
	}
	i=0;
	printf("enter elements of 2nd matrix : ");
	while(i<r)
	{
		j=0;
		while(j<c)
		{
			scanf("%d",&b[r][c]);
			j++;
		}
		i++;
	}
	i=0;
	j=0;
	int rc=0;
	do
	{
		j=0;
		do
		{
			rc=0;
			do
			{
				c[i][j]+=a[i][j]*b[rc][j]
				rc++;
			}while(rc<r);
			j++;
		}while(j<c);
		i++;
	}while(i<r);
	
	for(i=0;i<r;i++)
	{
		for(j=0;j<c;j++)
		{
			printf("%d  ",a[i][j]);
		}
		printf("\t");
		for(j=0;j<c;j++)
		{
			printf("%d  ",b[i][j]);
		}
		printf("\t");
		for(j=0;j<c;j++)
		{
			printf("%d  ",b[i][j]);
		}
		printf("\n");
	}
	return 0;
}
