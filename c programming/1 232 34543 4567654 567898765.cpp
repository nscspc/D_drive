/*

        1
      2 3 2
    3 4 5 4 3
  4 5 6 7 6 5 4
5 6 7 8 9 8 7 6 5

*/
#include<stdio.h>
int main()
{
	int i,j,k,x,a,b,nr,c=0;
	printf("enter no. of rows : ");
	scanf("%d",&nr);
	a=0;
	b=0;
	for(i=1;i<=nr;++i)
	{
		if(i>=6)
		c++;
		for(j=0;j<nr*2-2-a-c+15;++j)
		{
			printf(" ");
		}
		for(k=i;k<=i+b;++k)
		{
			printf("%d ",k);
		}
		for(x=k-2;x>=i;--x)
		{
			printf("%d ",x);
		}
		printf("\n");
		a+=2;
		b++;
	}
}
