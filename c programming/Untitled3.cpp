#include<stdio.h>
typedef struct
{
	int x;
	int y;
}a;
int main()
{
	a v,*p;
  p=&v;
	v.x=01;
	printf("%d",(*p).x);
  p->y=7410;
  printf("%d",v.y);
	return 0;
}
