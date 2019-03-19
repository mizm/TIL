package test1;

public class e_7jin {
	public static void get(int n, int k)
	{
		if(n < k)
		{
			System.out.print(n);
			return;
		}
		get(n/k,k);
		System.out.print(n%k);
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int item = 123;
		get(item,7);

	}

}
