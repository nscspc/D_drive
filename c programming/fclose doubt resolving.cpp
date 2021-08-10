#include<stdio.h>
int main()
{
	FILE *f;
	f=fopen("open.txt","w");
	if(f==NULL)
	printf("cannot open file .");
	else{
	printf("jakjjf");
	fprintf(f,"%d",1);
	fclose(f);}
}
