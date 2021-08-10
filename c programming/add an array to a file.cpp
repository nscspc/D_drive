#include<stdio.h>
int main()
{
	char a[]={'q','w','e','r','t','y'};
	int b[]={1,2,3,4,5};
	FILE *file;
	file=fopen("arr.txt","w+");
	if(file==NULL)
	{
		printf("cannot open file .");
		return 0;
	}
	else
	{
		fputs(b,file);
	}
	fclose(file);
	return 0;
}
