#include<stdio.h>
int main()
{
	FILE *file;
	int i,sum=0,c=0;
	char s[10];
	
	file=fopen("emp.txt","r");
	
	if(file==NULL)
	{
		printf("cannot open file .");
		return 0;
	}
	else
	{
		rewind(file);	
		while(feof(file)==0)
		{
			fscanf(file,"%s",&s);
			fscanf(file,"%d",&i);
			sum=sum+i;
			c++;
			
		}
		printf("average salary of all the employees : %f",(float)sum/c);
		fclose(file);
	}
	
	return 0;

}
