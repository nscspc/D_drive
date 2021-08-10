#include<stdio.h>
int main()
{
	FILE *file;
	int arr[10]={1,2,3,4,5,5,4,5,5,4};
		
	file=fopen("binary.txt","wb");
	if(file==NULL)
	{
		printf("cannot open file .");
	}
	else
	{
		fwrite(arr,sizeof(arr),1,file);
	}
	fclose(file);
	return 0;
}
