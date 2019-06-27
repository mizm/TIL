// ConsoleApplication1.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//
# define _CRT_SECURE_NO_WARNINGS
// #include "pch.h"
#include <iostream>
using namespace std;

int r, n, s, map[101][101][3] = { 0, };
int res = 0;
int dx[5] = { 0,0,0,1,-1 };
int dy[5] = { 0,-1,1,0,0 };
bool is_safe(int y, int x) {
	if (y > 0 && y <= r && x > 0 && x <= s) return true;
	else return false;
}
void fishing(int position)
{
	for (int i = 1; i <= r; i++)
	{
		if (map[position][i][2] > 0)
		{
			res += map[position][i][2];
			map[position][i][2] = 0;
			map[position][i][0] = 0;
			map[position][i][1] = 0;
			break;
		}
	}
}
void go()
{
	int tmap[103][103][3] = { 0, };
	int ny = 0;
	int nx = 0;
	for (int j = 1; j <= r; j++)
	{
		for (int i = 1; i <= s; i++)
		{
			if (map[i][j][2] > 0)
			{
				nx = i;
				ny = j;
				if (map[i][j][1] <= 2)
				{
					for (int q = 0; q < map[i][j][0]; q++)
					{
						if (ny == 1) map[i][j][1] = 2;
						if (ny == r) map[i][j][1] = 1;
						ny += dy[map[i][j][1]];
					}
				}
				else
				{
					for (int q = 0; q < map[i][j][0]; q++)
					{
						if (nx == 1) map[i][j][1] = 3;
						if (nx == s) map[i][j][1] = 4;
						nx += dx[map[i][j][1]];
						
					}
				}
				if (tmap[nx][ny][2] < map[i][j][2])
				{
					tmap[nx][ny][0] = map[i][j][0];
					tmap[nx][ny][1] = map[i][j][1];
					tmap[nx][ny][2] = map[i][j][2];
				}
			}
		}
	}
	for (int j = 1; j <= r; j++)
	{
		for (int i = 1; i <= s; i++)
		{
			map[i][j][0] = tmap[i][j][0];
			map[i][j][1] = tmap[i][j][1];
			map[i][j][2] = tmap[i][j][2];
		}
	}
}
int main()
{
	//scanf_s("%d %d %d", &r, &s, &n);
	cin >> r >> s >> n;
	for (int i = 0; i < n; i++)
	{
		int a, b, c, d, e;
		cin >> a >> b >> c >> d >> e;
		map[b][a][0] = c;
		map[b][a][1] = d;
		map[b][a][2] = e;
	}
	for (int i = 1; i <= s; i++)
	{
		fishing(i);
		go();
	}
	printf("%d", res);
	return 0;
}
