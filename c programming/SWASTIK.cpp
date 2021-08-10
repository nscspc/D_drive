/*

* * * * *       *
        *       *
        *       *
		*       *
* * * *	* * * * *      
*       *     
*       *
*       *
*       * * * * *

*/

#include<stdio.h>
int main()
{
	int a,s,i,j;
	printf("enter size : ");
	scanf("%d",&s);
	for(a=0;a<s*2-1;a++)
	{
	for(i=0;i<s;i++)
	{
		if(i==s-1 || (i==0 && (a>=s && a<s*2-1)))
		printf("* ");
		else if(a==0 || a==s-1)
		printf("* ");
		else
		printf("  ");
		
	}
	for(j=0;j<s-1;j++)
	{
		if((a==s-1 || a==s*2-2) || ((a>=0 && a<s-1) && j==s-2))
		printf("* ");
		else
		printf("  ");
	}
	printf("\n");
	}
	return 0;
}
/*

* * *   *
    *   *
* * * * *
*   *
*   * * *    

*/
