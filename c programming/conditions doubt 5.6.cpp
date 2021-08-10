#include<stdio.h>
int main()
{
	int x=10;
	printf("%d",x==10 && x>10 && !x);
	printf("%d",x==10 || x>10 && !x);//firstly && operater is evaluated then ||
	printf("%d",x==10 && x>10 || !x);
	printf("%d",x==10 || x>10 || !x);
}
