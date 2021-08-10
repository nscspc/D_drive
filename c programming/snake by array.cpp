#include<stdio.h>
//#include<conio.h>
//#include<cstdlib>
//#include<windows.h>
#include<time.h>
#include<stdlib.h>
//using namespace std;
int main()
{
  float time;
	int i,j,k,b=1,c=9,x=0,y=1,z;
	char d=' ',t,arr[20][40];
	
	for(i=0;i<20;i++)
	{
		for(j=0;j<20;j++)
		{
			if(i==0 || i==19)
			{
				arr[i][j]='*';
        //if(j!=39 || i!=39)
				//arr[i+1][j+1]=' ';
			}
			else if(j==0 || j==19)
			{
				arr[i][j]='*';
			}
      else if(i==9 && (j==b||j==b+1))
      {
        arr[i][j]='*';
      }
			else
      {
        arr[i][j]=' ';
        arr[i+1][j+1]=' ';
      }
		}
	}
  for(k=0;k<26;k++)
  {
    //scanf("%d",&z);
    //time=clock();
    if(d==' ')
    d=getchar();

    if(d=='\0')
    {

    }

    //Clrscr();
	  system("clear");
    for(i=0;i<20;i++)
    {
	    for(j=0;j<20;j++)
	    {
        printf("%c ",arr[i][j]);
      }
      printf("\n");
    }
    if(d=='w')
    {
      t=arr[c][b+x];
      arr[c][b+x]=arr[c-y][b+1];
      arr[c-y][b+1]=t;
      if(k>17)
      {
        c--;
      }
      if(k>16)
      {
        y=2;
      }
      //b=19;
      x=1;
    }
    else if(k<16)
    {
      t=arr[9][b];
      arr[9][b]=arr[9][b+2];
      arr[9][b+2]=t;
      b++;
    }
    //printf("%d",b);
    //if(k>=16)
    /*if(d=='w')
    {
      t=arr[c][b+x];
      arr[c][b+x]=arr[c-y][b+1];
      arr[c-y][b+1]=t;
      if(k>17)
      {
        c--;
      }
      if(k>16)
      {
        y=2;
      }
      //b=19;
      x=1;
    }*/
    
    for(int a=0;a<=11111100;a++);
  }
}
