//program to print more than 1 values in text file using loop.

#include<stdio.h>
int main()
{
	FILE *file;
	int i;
	file=fopen("pps.txt","w");
	
	if(file==NULL)
	{
		printf("cannot open file .");
		
		return 0;
	}
	
	else
	{
		for(i=1;i<=20;i++)
		fprintf(file,"%d ",i);
		
		printf("file opened successfully .");
		
		fclose(file);
	}
	return 0;
}
