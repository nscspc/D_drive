#include <stdio.h>

int main(void) 
{
  FILE *file;
  char sname[20];
  file=fopen("student.txt","a");
  if (file==NULL)
  {
    printf("cannot open file .");
    return 0;
  }
  else
  {
  	do
    {
	  printf("enter name : ");
      gets(sname);
      fputs(sname,file);
	}while(sname[0]!='.');
  }
  fclose(file);
  return 0;
}
