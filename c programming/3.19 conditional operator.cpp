#include<stdio.h>
int main()
{
	for(int m=0;m<3;++m)
	{
		printf("%d\n",(m%2)?m:m+2);
	}
}
