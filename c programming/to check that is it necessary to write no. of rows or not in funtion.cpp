#include<stdio.h>
void check(int b[][],int m,int n)
{
	b[0][0]=10;
}
int main()
{
	int a[2][2]={{1,2},{2,3}};
	check(a[][],2);
	printf("%d",b[0][0]);
}
