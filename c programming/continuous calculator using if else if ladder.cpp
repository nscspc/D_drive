#include<stdio.h>

int main()
{
  float n1,n2;
  char op;

  printf("enter equation : ");
  scanf("%f%c%f",&n1,&op,&n2);
condition:
while(op!='Q')
{
	if(op=='+')
	{
		printf("%f",n1+n2);
		n1=n1+n2;
	}
	else if(op=='-')
	{
		printf("%f",n1-n2);
		n1=n1-n2;
	}
	else if(op=='*')
	{
		printf("%f",n1*n2);
		n1=n1*n2;
	}
	else if(op=='/')
	{
		printf("%f",n1/n2);
		n1=n1/n2;
	}
	else
	{
		printf("invalid operator used.....");
		op='Q';
		goto condition;
	}
  /*switch(op)
  {
    case'+':printf("%f",n1+n2);n1=n1+n2;break;
    case'-':printf("%f",n1-n2);n1=n1-n2;break;
    case'*':printf("%f",n1*n2);n1=n1*n2;break;
    case'/':printf("%f",(float)n1/n2);n1=n1/n2;;break;
    default:op='q';
  }*/
  scanf("%c",&op);
  //scanf("%f",&n2);
}
return 0;
}
