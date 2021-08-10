#include<stdio.h>
#include<math.h>
int main()
{
	int a,b,x[20][360];
	//printf("enter size of square : ");
	//scanf("%d",&x);	
	for(a=0;a<360;a=a+90)
	{
		b=sin(a);
		if(b==0)
		{
			x[10][a]=b;
		}
		else if(b==1)
		{
			x[0][a]=b;
		}
		else if(b==-1)
		{
			x[20][a]=b;
		}
		
		printf("\n");
	}
	//for(a=0;a<360;a=a+90)
	for(b=0;b<20;b++)
	for(a=0;a<360;a=a+90)
	printf("%d",x[b][a]);
}
