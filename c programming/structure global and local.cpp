#include<stdio.h>
/*struct a
	{
		int a1=100;
		int a2;
		int a3;
	}av;*/
struct a structaccess(struct a b)
{
	printf("%d",b.a1);
}
 main()
{
	struct a
	{
		int a1=100;
		int a2;
		int a3;
	}av;
	structaccess(struct a av);
	printf("%d",av.a1);
}

