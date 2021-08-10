#include<stdio.h>
int main()
{
	int *fptr;
	
	fptr=fopen("exp","w");
	printf("%d\n",fptr);
	if(fptr==NULL)
	{
		printf("cannot open file .");
		return 0;
	}
	else
	{
		printf("file opened successfully .");
	}
	fclose(fptr);
	return 0;
}
