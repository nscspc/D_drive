#include<stdio.h>

struct employee
{
	int emp_id;
	char emp_name[20];
	int salary;
}e[10];

void add(void);
void search(void);
void modify(void);
void del(void);
void show(void);
	
int i,sum,c,n,salary,id;
char name[20],searchh[20];

//FILE *file;
//file=fopen("emp.txt","a");

int main()
{
	FILE *file;
	//int i,sum,c,n,search,name,salary;
		
	file=fopen("empdata.txt","a");
	if(file==NULL)
	{
		printf("cannot open file .");
		return 0;
	}
	else
	{	
		printf("           ** EMPLOYEE MANAGEMENT SYSTEM **\n1. Search Record\n2. Show All Records\n3. Add Record\n4. Modify Record\n5. Delete Record\n6. Exit");
		scanf("%d",&c);
		
		if(c==1)
		{
			search();
			printf("%d",11);
		}
		else if(c==2)
		{
			show();
			printf("%d",11);
		}
		else if(c==3)
		{
			add();	
		}
		else
		{
			printf("%d",1);
		}
	fclose(file);
	}
	return 0;
}

void add(void)	
{
	FILE *file;
	file=fopen("empdata.txt","a");
	printf("\nhow many employee record do you want to enter : ");
	scanf("%d",&n);
		
	for(i=0;i<n;i++)
	{
		printf("\nenter employee ID : ");
		scanf("%d",&e[i].emp_id);
		fprintf(file,"%d",e[i].emp_id);
			
		printf("\nemployee name : ");
		scanf("%s",e[i].emp_name);
		fprintf(file,"%s  ",e[i].emp_name);
			
		printf("\nenter salary : ");
		scanf("%d",&e[i].salary);
		fprintf(file,"%d",e[i].salary);
	}
	printf("\nrecord added successfully .");
	fclose(file);
}
		
void search(void)
{
	FILE *file;
	file=fopen("empdata.txt","r");
	printf("enter the name of whom you want to search record : ");
	scanf("%s",searchh);
			
	/*while(feof(file)==0)
	{
		fscanf(file,"%d",&id);
		printf("%d",id);
		fscanf(file,"%s",name);
		fscanf(file,"%d",&salary);
		if(searchh==name)
		{
			printf("\nID      NAME      SALARY");
			printf("\n%d       %s         %d",id,name,salary);
			break;
		}
	}*/
	for(i=0;i<10;i++)
	{
		if(searchh==e[i].emp_name)
		{
			printf("%s",e[i].emp_name);
			break;
		}
	}
	fclose(file);
}

void show(void)
{
	FILE *file;
	file=fopen("empdata.txt","r");
	printf("\nID      NAME      SALARY");
	while(feof(file)==0)
	{
		fscanf(file,"%d",&id);
		fscanf(file,"%s",name);
		fscanf(file,"%d",&salary);
		printf("\n%d       %s         %d",id,name,salary);
	}
	fclose(file);
}

void modify(void)
{
	printf("enter the name of whom you want to modify record : ");
	scanf("%s",search);
	
	
	
}

