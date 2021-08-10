#include<stdio.h>
int main()
{
	FILE *fptr;
	float marks;
	char name[50],subject[50];
	
	fptr=fopen("student.txt","a");
	if(fptr==NULL)
	{
		printf("cannot open file .");
	}
	else
	{
		printf("enter name : ");
		scanf("%s",name);
		printf("enter subject : ");
		scanf("%s",subject);
		printf("enter marks : ");
		scanf("%f",&marks);
		
		fprintf(fptr,"%s",name);
		fprintf(fptr,"%s",subject);
		fprintf(fptr,"%f",marks);	
	}
	
}
