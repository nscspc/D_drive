#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define n 0
int main()
{
    char *buffer;

    //allocating memory//
    if((buffer=(char*)malloc(10))==n)
    {
        printf("malloc failed.\n");
        exit(1);
    }
    printf("buffer of size %d created \n",_msize(buffer));
    strcpy(buffer,"hyderabad");
    printf("buffer contains : %s\n",buffer);

    if((buffer=(char*)realloc(buffer,15))==n)
    {
        printf("reallocation failed\n");
        exit(1);
    }
    printf("buffer size modified\n");
    printf("buffer still contains : %s\n",buffer);

    strcpy(buffer,"secunderabadhgjhhhhjjhjkjkkjhkj");
    printf("buffer now contains : %s\n",buffer);

    return 0;
}