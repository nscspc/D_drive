#include <stdio.h>

int main()
{
  double n1,n2;
  char op;
  int loop;

  printf("enter equation : ");
  scanf("%lf%c%lf",&n1,&op,&n2);

  for(loop=1;loop>0;loop++)
  {
    switch(op)
    {
      case '+':printf("%lf",n1=n1+n2);break;
      case '-':printf("%lf",n1=n1-n2);break;
      case '*':printf("%lf",n1=n1*n2);break;
      case '/':printf("%lf",n1=n1/n2);break;
      
      default:loop=-1;
    }
    if(loop!=-1)
    scanf(" %c%lf",&op,&n2);
    
  }
  return 0;

}
