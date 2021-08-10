#include<stdio.h>
//#include<conio.h>
	struct book
	{
		int bookid;
		char bname[100];
		int bprice;
	}b;
int main(void)
{
	printf("enter book id : ");
	scanf("%d",&b.bookid);
	printf("enter book name : ");
	//scanf("%s",b.bname);
	gets(b.bname);
	puts("enter book price : ");
	scanf("%d",&b.bprice);
	
	printf("%d",b.bookid);
	printf("%s",b.bname);
	printf("%d",b.bprice);
}
