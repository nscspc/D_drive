#include<stdio.h>
#include<stdlib.h>
#define N 0
int main()
{
	int *p,*table;
	int size;
	printf("\nwhat is size of table?");
	scanf("%d",&size);
	printf("\n");
	
	if((table=(int*)malloc(sizeof(int)*size))==N)
	{
		printf("no space available \n");
		exit(1);
	}
	printf("\naddress of the first byte is %u\n",table);
	printf("input table values\n");
	for(p=table;p<table+size+2;p++)
	{
		scanf("%d",p);
	}
	for(p=table;p<table+size+2;p++)
	{
		printf("%d is stored at address %u \n",*p,p);
	}
}
	
