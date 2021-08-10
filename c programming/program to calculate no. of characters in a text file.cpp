//program to find out the no. of characters in a text file.

#include<stdio.h>
int main()
{
	FILE *file;
	int i,c=0;
	
	file=fopen("what.txt","r");
	if(file==NULL)
	{
		printf("cannot open file .");
	}
	else
	{
		while(feof(file)==0)
		{
			fscanf(file,"%c",&i);
			c++;
		}
		printf("no. of characters in file : %d",c-1);
	} 
}
