// sw 1240 ´Ü¼ø2Áø
#include<iostream>
using namespace std;

int main() {
	int t = 0;
	cin >> t;
	for(int tc=1; tc<t+1;tc++)
	{
		int n = 0;
		int m = 0;
		int bitcode[] ={13,25,19,61,35,49,47,59,55,11};
		cin >> n >> m;
		int code[50][100];
		int res[20] = {0,};
		int rk=0;
		int tmp = 0;
		for(int i = 0; i < n; i++)
		{
			char chk[100];
			cin >> chk;
			
			for(int j = 0; j < m; j++)
			{
				code[i][j] = int(chk[j])-48;
				if(code[i][j] && tmp == 0)
					tmp = 1;
			}
			if(tmp==1)
			{
				int k=0;
				int st = 0;
				int temp = 0;
				for(int j = m-1; j > -1; j--)
				{
					if(code[i][j] == 1)
					{
						temp += 1<<k;
						if(st == 0) st = 1;
					}
					if(st) k++;
					
					if(k==7)
					{
						for(int o=0; o<10; o++)
						{
							if(bitcode[o] == temp)
							{
								res[rk] = o;
								break;
							}
						}
						temp = 0;
						k = 0;
						rk++;
					}				
				}
				tmp = -1;
			}
		}
//		for(int i = 0; i < rk; i++)
//		{
//			cout << res[i] << " ";
//		}
		int c1=0,c2=0;
		for(int i = 1; i < rk; i++)
			if(i%2) c2+= res[i];
			else c1 += res[i];
		if((c2*3+c1+res[0]) % 10 == 0)
			cout<<"#"<<tc <<" "<< c1+c2+res[0]<< "\n";
		else
			cout<<"#"<<tc<<" "<<0<<"\n";
	}
//	for(int i = 0; i < n; i++)
//	{
//		for(int j = 0; j < m; j++)
//		{
//			cout << code[i][j] << " ";
//		}
//		cout<<endl;
//	}
}
