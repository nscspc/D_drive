#include<stdio.h>

void array(int arr2[])
{
	arr2[2]=4;
}

int main()
{
	int arr[4]={1,2,3,4},i;
	array(arr);
	printf("%d",arr[0]);
	for(i=0;i<4;i++)
	{
		printf("%d",arr[i]);
	}
	return 0;
}
