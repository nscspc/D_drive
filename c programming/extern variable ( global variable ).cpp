#include<stdio.h>
extern void c(void)
{
	extern int yj;
	printf("%d",yj);	
}
int main()
{
	extern int yj;
	printf("%d",yj);
	c();
	return 0;
}
int yj=45;

