#include <stdio.h>

int main(void) 
{
  FILE *file;
  char ch;
  file=fopen("student.txt","r");
  if (file==NULL)
  {
    printf("cannot open file .");
    return 0;
  }
  else
  {
    while(feof(file)==0)
    {
      ch=fgetc(file);
      printf("%c",ch);
    }
  }
  fclose(file);
  return 0;
}
