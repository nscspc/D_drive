/*
          @       @
        @   @   @   @
      @       @       @
    @           @       @
  @       @       @       @
    @   @   @   @       @
      @       @       @   
    @       @   @   @   @ 
  @       @       @       @
    @       @           @
      @       @       @
        @   @   @   @
          @       @
*/

#include<stdio.h>
int main()
{
	char character;
	printf("enter the character that you want to print in pattern : ");
	scanf("%c",&character);
	int r,c,i,j,a,b,d,k;
	i=10;j=18;
	k=10;d=18;
	for(r=0;r<13;r++)
	{
		for(c=1;c<=26;c++)
		{
			if((r==0 && (c==10 || c==18))||(r==13 && (c==18 || c==10)))
			printf("%c",character);
			else if((r==3 && c==10+2) || (r==9 && c==18-2))
			printf(" ");
			else if(((c==i || c==j)||(c==k || c==d))||((c==8 && r==5)||(c==20 && r==7)))
			printf("%c",character);
			/*else if((c==8 && r==5)||(c==20 && r==7))
			printf("%c",character);*/
			else
			printf(" ");
		}
		if((r>=0 && r<4)||(r>=6 && r<8))
		{		// 0  1   2   3
		i=i+2;  //12  14  16  18
		j+=2;   //20  22  24  26
		k-=2;   //8   6   4   2
		d-=2;   //16  14  12  10
		}
		else
		{
			i-=2;
			j-=2;
			k+=2;
			d+=2;
		}
		printf("\n");	
	}
	return 0;
}
          
