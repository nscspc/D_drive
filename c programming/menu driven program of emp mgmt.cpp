#include<stdio.h>

struct employee
{
	int emp_id;
	char emp_name[20];
	int salary;
}e;

void add(void);
void search(void);
void modify(void);
void del(void);
void show(void);
	
int i,sum,c,n,salary,id,modid,position,position1,position2;
char name[20],searchh[20];
char m;

//FILE *file;
//file=fopen("emp.txt","ab");

int main()
{
	FILE *file;
	//int i,sum,c,n,search,name,salary;
		
	file=fopen("empdat.dat","ab");
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
		}
		else if(c==2)
		{
			show();
		}
		else if(c==3)
		{
			add();	
		}
    else if(c==4)
		{
			modify();	
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
	file=fopen("empdat.dat","ab");
	printf("\nhow many employee record do you want to enter : ");
	scanf("%d",&n);
		
	for(i=0;i<n;i++)
	{
		printf("\nenter employee ID : ");
		scanf("%d",&e.emp_id);
		//fprintf(file," %d",e[i].emp_id);
			
		printf("\nemployee name : ");
		scanf("%s",e.emp_name);
		//fprintf(file," %s ",e[i].emp_name);
			
		printf("\nenter salary : ");
		scanf("%d",&e.salary);
		//fprintf(file,"%d",e[i].salary);//after %d there should be no space.
		
		fwrite(&e,sizeof(e),1,file);
	}
	printf("\nrecord added successfully .");
	fclose(file);
}
		
void search(void)
{
	FILE *file;
	file=fopen("empdat.dat","rb");
	printf("enter the name of whom you want to search record : ");
	scanf("%s",searchh);
			
	while(feof(file)==0)
	{
    c=0;
		/*fscanf(file,"%d",&id);
		fscanf(file,"%s",name);
		fscanf(file,"%d",&salary);*/
		fread(&e,sizeof(e),1,file);
    	for(i=0;i<20;i++)
		{
      		if(searchh[i]==e.emp_name[i])
      		{
        		c++;
      		}
    	}
    	if (c==20)
		{
			printf("\nID      NAME      SALARY");
			printf("\n%d       %s         %d",e.emp_id,e.emp_name,e.salary);
      		break;
		}
	}
	fclose(file);
}

void show(void)
{
	FILE *file;
	file=fopen("empdat.dat","rb");
	printf("\nID    NAME     SALARY");
	while(feof(file)==0)
	{
		//printf("\n%d       %s         %d",e.emp_id,e.emp_name,e.salary);
		fread(&e,sizeof(e),1,file);
		printf("\n%d    %s     %d",e.emp_id,e.emp_name,e.salary);
	}
	fclose(file);
}

void modify(void)
{
  FILE *file;
  file=fopen("empdat.dat","rb");
  printf("enter the ID of whom you want to modify record : ");
	scanf("%d",&modid);
  while(feof(file)==0)
	{
  		fread(&e,sizeof(e),1,file);
    /*for(i=0;i<10;i++)
	{
      if(searchh[i]==name[i])
      {
        c++;
      }*/
      if(e.emp_id==modid)
		{
			printf("\nID      NAME      SALARY");
			printf("\n%d       %s         %d",e.emp_id,e.emp_name,e.salary);
			break;
		}
	}
  printf("\nenter (n) to modify name and enter (s) to modify salary : ");
  scanf("%s",&m);
  //m='n';
  if (m=='n')
  {
    printf("enter new name : ");
    scanf("%s",name);
    //rewind(file);
    fseek(file,-40,SEEK_CUR);
    
    while(feof(file)==0)
    {
      position=ftell(file);
      fread(&e,sizeof(e),1,file);
      position1=ftell(file);
      if (id==e.emp_id)
      {
      	printf("%d",i);
      	position2=position1-position;
        break;
      }
    }
    position1=position1-position2;
    fseek(file,position1,SEEK_SET);
    fwrite(&id,sizeof(id),1,file);
    fwrite(&name,sizeof(name),1,file);
  }
  fclose(file);	
}

