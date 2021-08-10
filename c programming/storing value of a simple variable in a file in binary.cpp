#include<stdio.h>
/*struct student
{
	char name[20];
	int rollno;
	float per;
}*/
int main()
{
	int s=12345;
	FILE *file;
	file=fopen("stu.dat","rb");
	if(file==NULL)
	{
		printf("cannot open file");
	}
	else
	{
		fread(&s,sizeof(s),1,file);
		printf("%d",s);
		//fwrite(&s,sizeof(s),1,file);
	}
	return 0;
}
