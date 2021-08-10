#include<stdio.h>
int main()
{
	int c;
	float f;
	
	printf("enter temperature in celcius : ");
	scanf("%d",&c);
	
	f=(c*9/5)+32;
	
	printf("temp in fahrenheit : %f",f);
	
	return 0;
}
