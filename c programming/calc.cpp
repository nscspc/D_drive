#include<stdio.h>
int main()
{
	float a,b,i;
	char s;
	printf("enter : \n");
	scanf("%f",&a);
	scanf("%c",&s);
	scanf("%f",&b);
	for(i=1;i>0;i++)
	{
		switch(s)
		{
			case '+':printf("%f\n",a+b);break;
			case '*':printf("%f\n",a*b);break;
			case '-':printf("%f\n",a-b);break;
			case '/':printf("%f\n",a/b);break;
			//default : i=-10;
		}
		scanf("%f",&a);
	scanf("%c",&s);
	scanf("%f",&b);
		
	}
}
