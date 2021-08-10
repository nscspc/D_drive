#include<stdio.h>
#include<string.h>
int main()
{
	int a;
	char b,c,d;
	b=getchar();//ERROR if :- |getc(b);| or |b=getc();|
	//putchar(getchar());
	//putchar(getchar());
	//fflush(); :- not works.
	c=getchar();
	d=getchar();
	//error :- a=getw(); //error if :- getw(a);
	putchar(b);
	putchar(c);
	putc(d);	
}
