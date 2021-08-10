#include <stdio.h>
int main()
{
	int n1,n2,s;
	
	printf("enter value of first(n1) variable : ");
	scanf("%d",&n1);
	printf("enter value of second(n2) variable : ");
	scanf("%d",&n2);
	
	printf("value of first variable n1 : %d\nvalue of second variable n2 : %d",n1,n2);
	
	s=n1+n2;
	n1=s-n1;
	n2=s-n2;
	
	printf("After swapping values of variables :-\nvalue of first variable n1 : %d\nvalue of second variable n2 : %d",n1,n2);
	
	return 0;
}
