#include<stdio.h>
int main()
{
	FILE *file;
	char ch;
	
	file=fopen("emp.txt","w");
	if(file==NULL)
	{
		printf("cannot open file .");
	}
	else
	{
		printf("opened successfully\n\n");
		printf("enter a character : ");
		
		do
		{
			scanf("%c",&ch);
			putc(ch,file);
			
		}while();
		
		fclose(file);
	}
}
