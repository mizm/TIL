#include "pch.h"
/////////////////////////////////////////////////////////////////////////////////////////////
// �⺻ �����ڵ�� ���� �����ص� ���� �����ϴ�. ��, ����� ���� ����
// �Ʒ� ǥ�� ����� ���� �ʿ�� �����ϼ���.
// ǥ�� �Է� ����
// int a;
// float b, c;
// double d, e, f;
// char g;
// char var[256];
// long long AB;
// cin >> a;                            // int ���� 1�� �Է¹޴� ����
// cin >> b >> c;                       // float ���� 2�� �Է¹޴� ���� 
// cin >> d >> e >> f;                  // double ���� 3�� �Է¹޴� ����
// cin >> g;                            // char ���� 1�� �Է¹޴� ����
// cin >> var;                          // ���ڿ� 1�� �Է¹޴� ����
// cin >> AB;                           // long long ���� 1�� �Է¹޴� ����
/////////////////////////////////////////////////////////////////////////////////////////////
// ǥ�� ��� ����
// int a = 0;                            
// float b = 1.0, c = 2.0;               
// double d = 3.0, e = 0.0; f = 1.0;
// char g = 'b';
// char var[256] = "ABCDEFG";
// long long AB = 12345678901234567L;
// cout << a;                           // int ���� 1�� ����ϴ� ����
// cout << b << " " << c;               // float ���� 2�� ����ϴ� ����
// cout << d << " " << e << " " << f;   // double ���� 3�� ����ϴ� ����
// cout << g;                           // char ���� 1�� ����ϴ� ����
// cout << var;                         // ���ڿ� 1�� ����ϴ� ����
// cout << AB;                          // long long ���� 1�� ����ϴ� ����
/////////////////////////////////////////////////////////////////////////////////////////////

#include<iostream>


using namespace std;
int res = 987654321;
void search(int Data[16][16],int a, int n)
{
	int item[16];
	for (int i = 0; i < n; i++)
	{
		if (a & 1 << i) item[i] = 1;
		else item[i] = 0;
	}
	//printf("%d\n", a);
	//for (int i = 0; i < n; i++)
	//{
	//	printf("%d  ", item[i]);
	//}
	//printf("\n");
	int temp1 = 0;
	int temp2 = 0;
	for (int i = 0; i < n-1; i++)
	{
		if (item[i] == 1)
		{
			for (int j = i + 1; j < n; j++)
			{
				if (item[j] == 1)
				{
					temp1 += Data[i][j];
					temp1 += Data[j][i];
					//printf("%d %d %d %d\n", Data[i][j], Data[j][i],i,j);
				}
			}
		}
	}
	for (int i = 0; i < n - 1; i++)
	{
		if (item[i] == 0)
		{
			for (int j = i + 1; j < n; j++)
			{
				if (item[j] == 0)
				{
					temp2 += Data[i][j];
					temp2 += Data[j][i];
					//printf("%d %d %d %d\n", Data[i][j], Data[j][i], i, j);
				}
			}
		}
	}
	//printf("%d %d \n\n", temp1, temp2);
	temp1 -= temp2;
	if (temp1 < 0)
		temp1 *= -1;
	if (temp1 < res)
		res = temp1;
}
int main(int argc, char** argv)
{
	int test_case;
	int T;
	/*
	   �Ʒ��� freopen �Լ��� input.txt �� read only �������� �� ��,
	   ������ ǥ�� �Է�(Ű����) ��� input.txt ���Ϸκ��� �о���ڴٴ� �ǹ��� �ڵ��Դϴ�.
	   //�������� �ۼ��� �ڵ带 �׽�Ʈ �� ��, ���Ǹ� ���ؼ� input.txt�� �Է��� ������ ��,
	   freopen �Լ��� �̿��ϸ� ���� cin �� ������ �� ǥ�� �Է� ��� ���Ϸκ��� �Է��� �޾ƿ� �� �ֽ��ϴ�.
	   ���� �׽�Ʈ�� ������ ������ �Ʒ� �ּ��� ����� �� �Լ��� ����ϼŵ� �����ϴ�.
	   freopen �Լ��� ����ϱ� ���ؼ��� #include <cstdio>, Ȥ�� #include <stdio.h> �� �ʿ��մϴ�.
	   ��, ä���� ���� �ڵ带 �����Ͻ� ������ �ݵ�� freopen �Լ��� ����ų� �ּ� ó�� �ϼž� �մϴ�.
	*/
	//freopen("input.txt", "r", stdin);
	cin >> T;
	/*
	   ���� ���� �׽�Ʈ ���̽��� �־����Ƿ�, ������ ó���մϴ�.
	*/
	for (test_case = 1; test_case <= T; ++test_case)
	{
		res = 987654321;
		int Data[16][16];
		/////////////////////////////////////////////////////////////////////////////////////////////
		/*
			 �� �κп� �������� �˰��� ������ ���ϴ�.

		 */
		 /////////////////////////////////////////////////////////////////////////////////////////////
		int n = 0;
		cin >> n;
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				cin >> Data[i][j];
			}
		}
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				cout << Data[i][j] << " ";
			}
			cout << endl;
		}
		for (int i = 0; i < 1<<n; i++)
		{
			int k = 0;
			for (int j = 0; j < n; j++)
			{
				if (i & 1 << j) k += 1;
			}
			if(k==n/2) search(Data,i, n);
		}
		printf("#%d %d\n", test_case, res);

	}
	return 0;//��������� �ݵ�� 0�� �����ؾ��մϴ�.
}