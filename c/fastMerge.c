///A Faster merge sort
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

void printArray(int* a,int l,bool newline)
{
	printf("[");
	for(int i=0;i<l;i++)
		printf(" %d ",a[i]);
		
	if(newline)
		printf("]\n");
	else
		printf("]");
}
void insertionSort(int* a, int l)
{
	 int i, j, temp;
    for (i = 1; i < l; i++) {
        temp = a[i];
        j = i;
        while ((j > 0) && a[j - 1] > temp) 
        {
            a[j] = a[j - 1];
            j = j - 1;
        }
        a[j] = temp;
    }
}

void mergeTwo(int* a,int la,int* b,int lb,int* buf)
{	
	int ia,ib;
	ia=ib=0;
	
	int i;
	
	for(i=0; ia<la && ib<lb ; i++)
	{
		if(a[ia]<b[ib])
			buf[i]=a[ia++];
		else
			buf[i]=b[ib++];
	}
	for( ;ia<la;ia++)
		buf[i++]=a[ia];
	for( ;ib<lb;ib++)
		buf[i++]=b[ib];
	
	memcpy(a,buf,sizeof(int)*(la+lb));
	
}
void mergeSort_(int* a,int l, int* buf)
{
	if(l==1)
		return ;
	else if(l<27)
		insertionSort(a,l);
	else
	{
		int mid=l/2;
		
		mergeSort_(a, mid, buf);
		mergeSort_(a + mid, l - mid, buf);
		
		
		mergeTwo(a, mid, a + mid, l - mid , buf);
	}
}
void mergeSort(int* a,int l)
{
	int buf[l];

	mergeSort_(a,l,buf);
}
void randomArray(int* ret,int l)
{
	for(int i=0;i<l;i++)
		ret[i]=rand()%1000;
}
int cmp(const void* a,const void* b)
{
	return (int*)a-(int*)b;
}
int main()
{
	int l=1000000;
	#include "randomArr"
	randomArray(a,l);
	//printArray(a,l,true);
	//mergeSort(a,l);
	//qsort(a,l,sizeof(int),cmp);
	//printArray(a,l,true);
	
}
