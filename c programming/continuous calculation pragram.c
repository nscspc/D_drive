#include <stdio.h>

int main()
{
  float n1,n2;
  char op;

  printf("enter equation : ");
  scanf("%f%c%f",&n1,&op,&n2);

while(op!='Q')
{
  switch(op)
  {
    case'+':printf("%f",n1+n2);n1=n1+n2;break;
    case'-':printf("%f",n1-n2);n1=n1-n2;break;
    case'*':printf("%f",n1*n2);n1=n1*n2;break;
    case'/':printf("%f",(float)n1/n2);n1=n1/n2;;break;
    default:op='q';
  }
  scanf("%c%f",&op,&n2);
}
}
