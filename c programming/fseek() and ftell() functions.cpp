#include<stdio.h>
int main()
{
	FILE *file;
	int position;
	char ch;
	file=fopen("what.txt","r");
	if(file==NULL)
	{
		printf("cannot open file");
		return 0;
	}
	else
	{
		position=ftell(file);
		ch=getc(file);
		printf("%d %c\n",position,ch);
		
		fseek(file,0,SEEK_END);
		position=ftell(file);
		ch=getc(file);
		printf("%d %c\n",position,ch);
		
		fseek(file,+10,SEEK_SET);
		position=ftell(file);
		ch=getc(file);
		printf("%d %c\n",position,ch);
	}
	fclose(file);
}
