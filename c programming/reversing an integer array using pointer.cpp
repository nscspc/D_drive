#include<stdio.h>
int main()
{
	int a[5],*c,i,n,j=4,x;
	puts("enter 5 intergers in the array");
	for(i=0;i<5;i++)
	{
		scanf("%d",&a[i]);
	}
	for(i=0;i<4;i++)//0 1 2 3 4
	{
		x=a[0];//1 2 3 4 5
		c=&x;
		for(n=0;n<4-i;n++)//n<4 0123 //n<3 012  //n<2 01 //n<1
		{
			a[n]=a[n+1];//23455 //34551  //45521 //55321
		}
		a[j]=*c;//23451 //34521 //45321 //54321 //54321
		j--;//3 2 1 0
	}
	for(i=0;i<5;i++)
	printf("%d ",a[i]);
	return 0;
}
