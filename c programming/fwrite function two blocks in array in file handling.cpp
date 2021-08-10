#include<stdio.h>
int main()
{
	int i,arr[10]={1,2,3,4,56,7,8,9,41,2};
	FILE *file;
	char hash='#';
	file=fopen("array.dat","ab");
	if(file==NULL)
	{
		printf("cannot open file");
	}
	else
	{
		fwrite(hash,sizeof(char),1,file);
		//fwrite(arr,sizeof(arr),2,file);
		/*fread(arr,sizeof(arr),2,file);
		for(i=0;i<1000;i++)
		printf("%d",arr[i]);
	*/}
	return 0;

}
