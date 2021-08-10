#include<stdio.h>
//#include<conio.h>
#include<stdlib.h>
#define NULL 0
struct linked_list
{
    int number;
    struct linked_list *next;
};

int main()
{
    int i;
    typedef struct linked_list node;
    node *head;
    head=(node*)malloc(sizeof(node));
    //data input in linked list//
    printf("input data in the list\ntype -999 to end\n");
    for(i=1;i>0;i++)
    {
        scanf("%d",&head->number);
        if(head->number==-999)
        {
            head->next=NULL;
            i=-1000;
        }
        else
        {
            head->next=(node*)malloc(sizeof(node));
            head=head->next;
        }
    }

}