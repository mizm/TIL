#include<iostream>

using namespace std;

int (*turn(int mag[4][8], int m, int dr))[8]
{
	for(int i = 0; i < 8; i++)
		mag[m][i] = 0;
	return mag;
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
	cin>>T;
	/*
	   ���� ���� �׽�Ʈ ���̽��� �־����Ƿ�, ������ ó���մϴ�.
	*/
	for(test_case = 1; test_case <= T; ++test_case)
	{

		/////////////////////////////////////////////////////////////////////////////////////////////
		/*
			 �� �κп� �������� �˰��� ������ ���ϴ�.
		 */
		/////////////////////////////////////////////////////////////////////////////////////////////
		int magnetic[4][8];
		int t[2][20] = {{0}};
		int k = 0;
		cin >> k;
		for(int i = 0; i<4; i++)
		{
			for(int j=0; j<8; j++)
			{
				cin >> magnetic[i][j];
			}
		}
		for(int i = 0; i <k; i++)
		{
			int m,dr = 0;
			cin >> m >> dr;
//			printf("%d %d \n",a,b);
			magnetic = turn(magnetic,m,dr);
			for(int i = 0; i < 8; i++)
			{
				printf("%d,",magnetic[m][i]);
			}
			
		}

	}
	return 0;//��������� �ݵ�� 0�� �����ؾ��մϴ�.
}
