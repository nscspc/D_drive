#include<stdio.h>
int main()
{
	//int x=y=z=1,2,3;     //error
	int x,y,z;
	x=y=z=0,2,3;
	printf("%d %d %d",x,y,z);
}
