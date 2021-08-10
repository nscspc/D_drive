#include<stdio.h>
int main()
{
	int no;
	char name1[15],name2[15],name3[15];
		
	printf("enter : ");
//	scanf("%d %15c", &no, name1);werty
	scanf("%[^q]",name1);
	printf("%20s",name1);
}
