//program to print data in text file and as output also using feof and scanf function and rewind() function.

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
		
		rewind(file);
		
		while(feof(file)==0)/*feof(file pointer name) is a function which finds 'end of file constant' ,
								 when it finds it then it returns non - zero value , otherwise it returns 0.*/
		{
			fscanf(file,"%d",&i);// i variable stores integer data up to the value when data of another datatype do not comes.
			printf("%d ",i);
		}
		
		fclose(file);
	}
	return 0;
}
