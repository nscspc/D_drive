#include<stdio.h>
int main()
{
	FILE *file;
	int arr[10],i;
	file=fopen("binary.txt","rb");
	if(file==NULL)
	{
		printf("cannot open file .");
	}
	else
	{
		fread(arr,sizeof(arr),1,file);
		
		for(i=0;i<10;i++)
		{
			printf("%d",arr[i]);
		}
	}
	fclose(file);
	return 0;
}
