#include<stdio.h>

struct employee
{
	char emp_name[20];
	int salary;
};
	
int main()
{
	FILE *file;
	int i,sum,c,n;
		
	file=fopen("emp.txt","a");
	if(file==NULL)
	{
		printf("cannot open file .");
	}
	else
	{
		struct employee e[10];
		
		printf("how many employee details do you want to enter : ");
		scanf("%d",&n);
		
		for(i=0;i<n;i++)
		{
			printf("\nemployee name : ");
			scanf("%s",e[i].emp_name);
			
			fprintf(file,"%s  ",e[i].emp_name);
			printf("enter salary : ");
			scanf("%d",&e[i].salary);
			printf("%d",e[i].salary);
			fprintf(file,"%d",e[i].salary);
		}
	}
	fclose(file);
}
