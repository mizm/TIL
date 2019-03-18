#include<iostream>
using namespace std;



int main() {
	int item[] = {0x0,0xF,0x9,0x7,0xA,0x3};
//	int item = 0x0F97A3;
	int n = 6;
	int temp = 0;
//	while(item > 0)
//	{
//		printf("%d",item%2);
//		if(item%2 == 1)
//		{
//			temp*=2;
//			temp+=1;
//		}
//		item /=2;
////		n++;
////		if(n%7==0){
////			printf("%d\n",temp);
////			temp = 0;
////		}
//	}
	for(int i=0; i<sizeof(item)/sizeof(int); i++)
	{
		for(int j=3; j > -1; j--)
		{
			if(n == -1)
			{
				printf("%d\n",temp);
				temp = 0;
				n = 6;
			}
//			printf("%d %d \n",item[i] & 1 << j,1<<j);
			if(item[i] & 1 << j)
			{
				temp += 1<<n;
			}
			n--;	
		}
		if(i == sizeof(item)/sizeof(int)-1)
		{
			printf("%d",temp>>n+1);
		}
	}
	return 0;
}

