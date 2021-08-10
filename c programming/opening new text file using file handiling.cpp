//progrma to oppen new text file using file handling.

#include<stdio.h>
int main()
{
	FILE *file;//file is a pointer variable of FILE datatype which is used to perform various functions on file.
	
	file=fopen("pps3.txt","r");
	
	if(file==NULL)/*this condition is used for the situation when the file is not created and opened in "r" mode 
					then this condition gets true , as the given file does not exist so therefore file cannot be opened.*/ 
	{
		printf("cannot open file .");
		
		return 0;
	}
	
	else
	{
		printf("file opened successfully .");
		
		
	}
	fclose(file);
	return 0;
}
