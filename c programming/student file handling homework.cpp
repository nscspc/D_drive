#include<stdio.h>
int main()
{
	FILE *fptr;
	int n,i;
	struct student
	{
		float marks[5][1];
		char name[50];
		char subject[5][50];
	}s;
	/*float marks;
	char name[50],subject[50];*/
	
	fptr=fopen("student.txt","a");
	if(fptr==NULL)
	{
		printf("cannot open file .");
	}
	else
	{
		printf("of how many students do you want to enter the record : ");
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			printf("enter name : ");
			scanf("%s",s.name);
			for(j=0;j<5;j++)
			{
				printf("enter subject name: ");
				scanf("%s",s.subject[j][50]);
				printf("enter marks : ");
				scanf("%f",&s.marks[j][1]);
			}
		
			fprintf(fptr,"%s",name);
			fprintf(fptr,"%s",subject);
			fprintf(fptr,"%f",marks);
		}
	}
	
}
