//program to print data in text file using feof and scanf function.

#include<stdio.h>
int main()
{
	FILE *file;
	int i,c=0;
	file=fopen("pps.txt","r");
	
	if(file==NULL)
	{
		printf("cannot open file .");
		
		return 0;
	}
	
	else
	{
		while(feof(file)==0)/*feof(file pointer name) is a function which finds 'end of file constant' ,
								 when it finds it then it returns 1 , otherwise it returns 0.*/
		{
			fscanf(file,"%d",&i);// i variable stores integer data up to the value when data of another datatype do not comes.
			printf("%d ",i);
		}
		
		fclose(file);
	}
	return 0;
}
