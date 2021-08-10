#include<stdio.h>
int main()
{
	float c,f;
	
	printf("enter temperature in celcius : ");
	scanf("%f",&c);
	
	f=(c*9/5)+32;
	
	printf("temp in fahrenheit : %f",f);
	
	return 0;
}
