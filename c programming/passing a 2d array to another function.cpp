#include<stdio.h>
//int sum(int [] [c],int,int);
/*int sum(int arr[][c],int r,int c)
{
	int sum=0,j,i;
	for(i=0;i<r;i++)
	for(j=0;j<c;j++)
	sum+=arr[i][j];
	return sum;
}*/
int main()
{
  int r=2,c=2;
	int arr[r][c]=
	{
		{1,1},
		{2,2}
	};
  int sum(int [][2],int,int);
	printf("%d",sum(arr),r,c);
}
int sum(int arr[][2],int r,int c)
{
	int sum=0,j,i;
	for(i=0;i<r;i++)
	for(j=0;j<c;j++)
	sum+=arr[i][j];
	return sum;
}
