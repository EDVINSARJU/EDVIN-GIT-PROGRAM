#include<stdio.h>
#include<stdlib.h>
void enqueue();
void dequeue();
void display();
struct node
{
int data;
struct node *next;
}*head=NULL,*ptr;
void main()
{
 int choice=0;
    printf("\n QUEUE OPERATIONS\n");
    while(choice != 4)
    {
        printf("\n1.Enqueue\n2.Dequeue\n3.Display\n4.Exit");
        printf("\n Enter your choice \n");
        scanf("%d",&choice);
        switch(choice)
        {
            case 1:
            {
                enqueue();
                break;
            }
            case 2:
            {
                dequeue();
                break;
            }

            case 3:
            {
                display();
                break;
            }
            case 4:
            {
                printf("Exited");
                break;
            }
            default:  printf(" Enter a valid choice ");

    }
}
}
void enqueue()
{
    struct node *ptr,*temp;
    int item;
    ptr = (struct node*)malloc(sizeof(struct node));
    if(ptr == NULL)
    {
        printf("invalid\n");
    }
    else
    {
        printf("\nEnter the value?\n");
        scanf("%d",&item);
        ptr->data = item;
        if(head == NULL)
        {
            ptr -> next = NULL;
            head = ptr;
            printf("\n Inserted value to the queue ");
        }
        else
        {
            temp = head;
            while (temp -> next != NULL)
            {
                temp = temp -> next;
            }
            temp->next = ptr;
            ptr->next = NULL;
            printf("\nElement inserted to Queue");

        }
    }
}
void dequeue()
{
    struct node *ptr;
    if(head == NULL)
    {
        printf("\nQueue is empty\n");
    }
    else
    {
        ptr = head;
        head = ptr->next;
        free(ptr);
        printf("\nElements deleted from queue\n");
    }
}
void display()
{
    ptr = head;
    if(ptr == NULL)
    {
        printf("Queue is empty");
    }
    else
    {
        printf("\n The given Queue is  \n");
        while (ptr->next!=NULL)
        {
            printf("%d->",ptr->data);
            ptr = ptr -> next;
        }
         printf("%d->NULL",ptr->data);

    }
}
