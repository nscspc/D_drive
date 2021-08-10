#include<stdio.h>
int main()
{
	int a,i,n1,j,z,x,y,n,c,b,d;
  printf("enter n : ");
  scanf("%d",&n);
	n1=n+n-1;
	a=n1-2;
	b=0;
	d=0;
	c=0;
if(n>10)
{
c=n-10;
b=c+c;
}
	for(i=n1;i>n-1;i--)
	{
		if(c<=d)
		b=0;
		for(x=n;x>=i-n+1;x--)
		{	
			printf("%d",x);
		}
		for(y=0;y<a+b;y++)
		{
			printf(" ");
		}
		for(z=x+1;z<=n;z++)
		{
			if(z!=1)
			printf("%d",z);
			
		}
		a-=2;
		printf("\n");
		d++;
		b-=2;
		
	}
	if(n>10)
	{
		c=n-10;
		b=c;
	}
	d=1;
	a=1;
	for(i=2;i<=n;i++)
	{
		if(d<9)
		b=0;
		for(x=n;x>=i;x--)
		{	
			printf("%d",x);
		}
		for(y=0;y<a+b;y++)
		{
			printf(" ");
		}
		for(z=x+1;z<=n;z++)
		{
			printf("%d",z);
			
		}
		a+=2;
		printf("\n");
		if(d>=9)
			b+=2;
		d++;
	}
}
