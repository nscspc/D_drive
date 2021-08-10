#include<stdio.h>

void binary(int);//to calculate binary values.
void arrayprt(int [],int);//to print binary values stored in array in reverse order. 

int i=0;
int digit[100];//array to store binary values.

int main()
{
	int no;
	printf("enter the value in decimal that you want to convert in binary : ");
	scanf("%d",&no);
	binary(no);
	return 0;
}

void binary(int n)
{
	int remain;
	
  if (n>=2)
		{
			remain=n%2;
			n=n/2;
			digit[i]=remain;
			i++;
      binary(n);
		}
		else
		{
			digit[i]=n;
      arrayprt(digit,i);
		}
	}
	
  void arrayprt(int a[],int j)
	{
    if (j>=0)
		{
      printf("%d",a[j]);
      j--;
      arrayprt(digit,j);
    }
	}
