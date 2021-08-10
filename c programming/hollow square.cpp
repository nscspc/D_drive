#include<stdio.h>
int main()
{
	int a,b,s;
	printf("enter size of square : ");
	scanf("%d",&s);	
	for(a=1;a<s+1;a++)
	{
		for(b=1;b<s+1;b++)
		{	
			if(a==1 || a==s ||b==1 || b==s)
			printf("S ");
			else
			printf("  ");
			
		}
		printf("\n");
	}
}
