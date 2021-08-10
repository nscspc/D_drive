// program to check the user function declaration in main() function
#include<stdio.h>
#include<conio.h>
int main()
{
	int a=10000;
	/*int print(int b)
	{
		return b;
	}*/
	int print(int);
	printf("%d",print(a));
	//getch();
	return 1;
}
int print(int b)
{
	return b;
	getch();
}
