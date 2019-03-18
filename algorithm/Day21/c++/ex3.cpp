#include<iostream>
using namespace std;

int main() {
	int item[] = {0x0,0xD,0xE,0xC};
	int n = sizeof(item)/sizeof(int);
	int Data[16] = {0,};
	int passbit[] = {13,19,59,49,35,55,11,61,25,47};
	int temp = 0;
	for(int i=0; i<n; i++)
	{
		//    for(int j = 0; j < 6; j++)
		//    {
		//    	if
		//	}
			for(int j = 3; j>-1; j--)
			{
				if(item[i] & 1<<j)
				{
					Data[i*4+3-j] = 1;			
				}
			}
	}
	int start = -1;
	for(int i = 0; i < n*4; i++)
	{
		temp = 0;
		for(int j = 0; j < 6; j++)
		{
			if(Data[i+j] == 1)
			{
				temp += 1<<(5-j);
			}
		}
		for(int j = 0; j < 10; j++)
		{
			if(temp == passbit[j])
			{
				start = i;
				break;
			}
		}
		if(start > -1) break;
	}
	temp = 0;
//	printf("\n\n%d \n",start);
	for(int i = start; i < 4*n; i++)
	{
		if(Data[i] == 1)
		{
			temp += 1<<(5-(i-start) % 6);
//			printf("\n\n%d \n",temp);
		}
		if((i-start) % 6 == 5 )
		{
//			printf("kk\n\n%d \n",temp);
			for(int j = 0; j < 10; j++)
			{
				if(temp == passbit[j])
				{
					printf("%d ",j);
					temp = 0;
					break;
				}
			}
		}
	}
}
