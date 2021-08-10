#include<stdio.h>
int main()
{
	int no;
	char name1[15],name2[15],name3[15];
		
	printf("enter : ");
//	scanf("%d %15c", &no, name1);werty
	scanf("%[a-z || A-Z || 1-100]",name1);
	printf("%-010s",name1);
}qw
