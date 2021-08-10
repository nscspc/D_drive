#include<stdio.h>

struct sb
{
	char name[11];
  	int no;
  	float price;
};
int main()
{
	int n;
	printf("total no of diff types of items purchased : ");
	scanf("%d",&n);
	int m=n;
	float sum;
	float total[n];//total array is created in main() (not in struct sb) because value of n is inputted by the user in main() function.
	int l[n];
	int c=0;
	int a;
	int b;
	struct sb b1[n];//b1 array is the array of sb datatype.

	for(n=0;n<m;n++)
	{
    	printf("enter item name : ");
    	scanf("%s",b1[n].name);
    	printf("enter price of 1 item : ");
    	scanf("%f",&b1[n].price);
    	printf("enter quantity : ");
    	scanf("%d",&b1[n].no);
		c=0;
    	total[n]=total[n]+((b1[n].no)*(b1[n].price));
    	for(b=0;b<m;b++)
  		{
  			for(a=0;a<11;a++)
  			if (b1[b].name[a]==NULL)
  			break;
  			else
  			c=c+1;
  		}
  		l[n]=11-c;
  		printf("%d",c);
  		printf("%d",l[n]);
  	}
  
  	/*for(n=0;n<11;n++)
  	{
  		for(a=0;a<11;a++)
  		if (b1[n].name[a]==void)
  		break;
  		else
  		c=c+1;
  	}
  	l=11-c;*/
  	for(n=0;n<m;n++)
  	{
    	sum=sum+total[n];
  	}
  
  	printf("\n\nBILL DETAILS : \n");
  	for(n=0;n<m;n++)
  	{
  		printf("        %s",b1[n].name);
  		for(a=0;a<l[n];a++)
  		{
  			printf(" ");
		}
		printf(": %.2f\n",total[n]);
  	}
  	printf("_____________________________\n");
  	printf("   TOTAL           :  %.2f\n",sum);
  	printf("TAXES @13          :  %.2f\n",(sum*13/100));
  	printf("_____________________________");
}
