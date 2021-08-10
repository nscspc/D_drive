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
	int s;
  	printf("enter the character that you want to print in pattern : ");
	scanf("%c",&character);
	printf("enter size of pattern in integer : ");
	scanf("%d",&s);
	//printf("enter the character that you want to print in pattern : ");
	//scanf("%c",&character);
	
	int r,c,i,j,a,b,d,k,cn,cn2,rn;
	a=(s*2)+(s/2);//10 5
	b=(s*4)+(s/2);//18 9
	i=a;j=b;
	k=a;d=b;
  if(b%2==0)
  {
    cn=b-2;
    cn2=a+(s/2);
    rn=b/2;
  }
  else
  {
    rn=a-2;
    cn=b+1;
    cn2=a-(s/2);
  }
	for(r=0;r<(s*3)+1;r++)
	{
		for(c=1;c<=(s*6)+10;c++)
		{
			if((r==0 && (c==a || c==b))||(r==(s*3)+1 && (c==a || c==b)))
			printf("%c",character);
			else if((r==s/(s/2)+1 && c==cn2) || (r==rn && c==cn))//3 3r 12  4c      //9 3r  16  10
			printf(" ");
			else if(((c==i || c==j)||(c==k || c==d))||((c==s*2 && r==s+1)||(c==s*5 && r==(s*2)-1)))
			printf("%c",character);
			/*else if((c==8 && r==5)||(c==20 && r==7))
			printf("%c",character);*/
			else
			printf(" ");
		}
		if((r>=0 && r<s)||(r>=s+(s/2) && r<s*2))
		{		// 0  1   2   3                      0   1    3    4
		i=i+2;  //12  14  16  18                 7   9    9    11
		j+=2;   //20  22  24  26                 11  13   13   15
		k-=2;   //8   6   4   2                  3   1    1    3
		d-=2;   //16  14  12  10                 7   5    5    7
		}
		else
		{         // 2    3
			i-=2;   // 7    5
			j-=2;   // 11
			k+=2;   // 3
			d+=2;   // 7
		}
		printf("\n");	
	}
	return 0;
}
/*
      @   @
    @   @   @
  @   @   @   @
    @   @   @
  @   @   @   @
    @   @   @
      @   @
*/