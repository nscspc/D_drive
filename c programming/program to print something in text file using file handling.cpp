//program to print something in text file using file handling.

#include<stdio.h>
int main()
{
	FILE *file;
	
	file=fopen("pps.txt","w");
	
	if(file==NULL)
	{
		printf("cannot open file .");
		
		return 0;
	}
	
	else
	{
		fprintf(file,"%d",10);
		
		printf("file opened successfully .");
		
		fclose(file);
	}
	return 0;
}
