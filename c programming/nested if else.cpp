#include<stdio.h>
int main()
{
	int ram,shaam,dhaam;
	
	printf("age of ram,shaam,dhaam : ");
	scanf("%d%d%d",&ram,&shaam,&dhaam);
	
	if(ram>shaam)
	{
		if(ram>dhaam)
		{
			printf("ram is eldest");
		}
		else
		{
			printf("dhaam is eldest");
		}
	}
	else
	{
		if(shaam>dhaam)
		{
			printf("shaam is eldest");
		}
		else
		{
			printf("dhaam is eldest");
		}
	}
	printf("\n%d%d%d",ram,shaam,dhaam);
	return 0;//if some statement is written after return 0; statement then it will not be executed.
}
