#include <stdio.h>
int main()
{
	int l=1;
	while(l<=10)
	{
		if (l==5)/*if can be used without curly brackets if only one statement 
					is written in if condition otherwise if statement to be used is 
					more than one then curly brackets should be used.*/
		break;/*break statement is a statement used with control statements for executing the loop according to the user.
				break statement do not able to execute statements below it when the condition gets true and
				 takes out of the loop and stops the loop.*/
		printf("%d\n",l);
		l++;
	}
	return 0;
}
