//calulator program on 2 no.s :-

#include <stdio.h>

int main()

{
	int n1,n2;
    char sign;
	
	printf("enter equation : ");
	scanf("%d%c%d",&n1,&sign,&n2);
	
	switch(sign)
	{
		case'+':printf("%d",n1+n2);break;
		case'-':printf("%d",n1-n2);break;
		case'*':printf("%d",n1*n2);break;
		case'/':printf("%d",n1/n2);break;
		
	}
	
	return 0;
}
