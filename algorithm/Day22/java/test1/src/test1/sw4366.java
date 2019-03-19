package test1;
import java.util.Scanner;
public class sw4366 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();
		for(int test_case = 1; test_case <= T; test_case++)
		{
			String itemA = sc.nextLine();
			String itemB = sc.nextLine();
	
			System.out.println(itemA+itemB);
			
		}
	}

}
